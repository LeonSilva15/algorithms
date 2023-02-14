# Linear solution for the Fibonacci sequence
# Type of solution: Linear O( n )

def fibonacci( n ):
    operations = 0
    fibo = [ 0, 1 ] # First 2 elements by definition as fibo[ n, n + 1 ]
    for _ in range( n - 1 ): # Users input 1 as starting point instead of 0
        operations += 1
        # Update the sequence as fibo[ n + 1, n + ( n + 1 ) ]
        fibo = [ fibo[ 1 ], fibo[ 0 ] + fibo[ 1 ] ]
    return fibo[ 0 ], n, operations

# Standalone test
if __name__ == '__main__':
    number, position, operations = fibonacci( 10 )
    print( 'Number: {}'.format( number ) )
    print( 'Position: {}'.format( position ) )
    print( 'Operations: {}'.format( operations ) )
