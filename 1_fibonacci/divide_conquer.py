# Logarithmic solution for Fibonacci sequence
# Type of solution: Logarithmic O( Log( n ) )

# Use numpy to avoid matrix overflow and matrix dot product
import numpy as np

# The base matrix contains the representation of Fibonacci:
# [ f( n + 1 ), f( n )     ]
# [ f( n )    , f( n - 1 ) ]
BASE_MATRIX = np.array([ [1, 1], [1, 0] ], dtype=np.uint64) # Numpy matrix of 64bytes of unsigned integers

count = 0
def calculate( matrix, n ):
    global count
    # Base case
    if( n == 1 ):
        return matrix
    # Case having a pair exponential n
    if( n % 2 == 0 ):
        count += 1
        return calculate( np.dot( matrix, matrix ), n // 2 )
    # Case having odd exponentail n
    # Multiply the matrix by the product of the exponentiated matrix
    count += 2
    return np.dot( matrix, calculate( np.dot( matrix, matrix ), n // 2 ) )

def fibonacci( n ):
    return calculate( BASE_MATRIX, n )[ 1 ][ 1 ], n, count

if __name__ == '__main__':
    number, position, operations = fibonacci( 100 )
    print( 'Number: {}'.format( number ) )
    print( 'Position: {}'.format( position ) )
    print( 'Operations: {}'.format( operations ) )
