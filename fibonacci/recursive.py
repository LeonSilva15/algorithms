# Exponential solution for Fibonacci sequence
# Type of solution: Exponential o( 2^n )

# The sequence uses 0 and 1 as base case
base = [ 0, 1 ]

operations = 0
def calculate( n ):
    global operations
    operations += 1
    # Base case
    if( n <= 1 ):
        return base[ n - 1 ]
    # Calculate the previous two numbers using recursion
    return calculate( n - 1 ) + calculate( n - 2 )

# External function to count the operations
def fibonacci( n ):
    global operations
    operations = 0
    return calculate( n ), n, operations

# Standalone test
if __name__ == '__main__':
    number, position, operations = fibonacci( 4 )
    print( 'Number: {}'.format( number ) )
    print( 'Position: {}'.format( position ) )
    print( 'Operations: {}'.format( operations ) )
