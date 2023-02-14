from matplotlib import pyplot as plt
import numpy as np

def fibonacci( n ):
    count = 0
    fibo = [ 0, 1 ]
    for _ in range( n ):
        count += 1
        fibo = [ fibo[ 1 ], fibo[ 0 ] + fibo[ 1 ] ]
    return n, count

y = []
for i in range( 1, 31 ):
    y.append( fibonacci( i ) )

transposed = np.array( y ).T
x, y = transposed
fig, ax = plt.subplots( 1, 1 )
ax.plot( x, y, c = 'y' )
plt.autoscale( tight = True )
plt.title( "Análisis de Algoritmo Lineal (Iterativo)" )
plt.xlabel( "Número de Fibonacci" )
plt.ylabel( "Numero de Multiplicaciones" )
plt.show()
