from matplotlib import pyplot as plt
import numpy as np

def fibo_lineal( n ):
    count = 0
    fibo = [ 0, 1 ]
    for _ in range( n ):
        count += 1
        fibo = [ fibo[ 1 ], fibo[ 0 ] + fibo[ 1 ] ]
    return n, count

y = []
for i in range( 1, 100 ):
    y.append( fibo_lineal( i ) )

transposed = np.array( y ).T
x, y = transposed

def fibo_recursive( n ):
    global count
    count += 1
    if( n <= 1 ):
        return n
    return fibo_recursive( n - 1 ) + fibo_recursive( n - 2 )

y2 = []
for i in range( 1, 10 ):
    count = 0
    fibo_recursive( i )
    y2.append( ( i, count ) )


transposed2 = np.array( y2 ).T
x2, y2 = transposed2

BASE_MATRIX = [ [1, 1], [1, 0] ]

def fibo_matrix( matrix, n ):
    global count
    if( n == 1 ):
        return matrix
    if( n % 2 == 0 ):
        count += 1
        return fibo_matrix( np.dot( matrix, matrix ), n // 2 )
    count += 2
    return np.dot( matrix,fibo_matrix( np.dot( matrix, matrix ), n // 2 ) )

y3 = []
for i in range( 1, 100 ):
    count = 0
    fibo_matrix( BASE_MATRIX, i )
    y3.append( ( i, count ) )

transposed = np.array( y3 ).T
x3, y3 = transposed


fig, ax = plt.subplots(1,1)
ax.plot( x, y, c = 'y' )
ax.plot( x2, y2, c = 'r' )
ax.plot( x3, y3, c = 'g' )

plt.autoscale( tight = True )
plt.title( "Algorithms comparison: Linear vs Exponential vs Logarithmic" )
plt.xlabel( "Fibonacci" )
plt.ylabel( "Multiplications" )
plt.show()
