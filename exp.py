count = 0
def exp( x, n):
    global count
    # Base case
    if ( n == 1 ):
        print( x )
        return x
    # Even
    if ( n % 2 == 0 ):
        count += 1
        return exp( x * x, n // 2 )
    # Odd
    count += 2
    return x * exp( x * x, n // 2 )

print( exp( 2, 100 ), count )
