ops = 0
def exp( x, n ):
    global ops

    # Base case
    if ( n == 1 ):
        return x

    # Even
    if ( n % 2 == 0 ):
        ops += 1
        return exp( x * x, n // 2 )

    # Odd
    ops += 2
    return x * exp( x * x, n // 2 )

print( exp( 10, 5 ), ops )
