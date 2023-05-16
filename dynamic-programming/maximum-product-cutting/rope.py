from constants import DESIRED_LEN
from constants import PIECES

mem = {}

# Assume that evry cut is the most valuable
for piece in PIECES:
    mem[ piece[ 0 ] ] = {
        "pieces": [ piece ],
        "price": piece[ 1 ]
    }

# Look cutting the rope by equal pieces
for piece in PIECES:
    for cutSize in range( 2, DESIRED_LEN + 1 ):
        newCutSize = piece[ 0 ] * cutSize
        # Break when out of desired len
        if newCutSize > DESIRED_LEN:
            break

        newCutPrice = piece[ 1 ] * cutSize
        # print(mem[ newCutSize ])
        if newCutPrice > mem[ newCutSize ][ "price" ]:
            mem[ newCutSize ][ "pieces" ] = [ piece ] * cutSize
            mem[ newCutSize ][ "price" ] = newCutPrice

# Look completing the rope pieces with other cuts
for piece in PIECES:
    for cutSize in mem:
        newCutSize = piece[ 0 ] + cutSize
        # Break when out of desired len
        if newCutSize > DESIRED_LEN:
            break
        newCutPrice = piece[ 1 ] + mem[ cutSize ][ "price" ]

        if newCutPrice > mem[ newCutSize ][ "price" ]:
            mem[ newCutSize ][ "pieces" ] + [ piece ]
            mem[ newCutSize ][ "price" ] = newCutPrice

print( mem )
print( mem[ DESIRED_LEN ] )
