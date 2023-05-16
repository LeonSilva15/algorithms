from constants import CAPACITY
from constants import OBJECTS

# Solve from the smallest capacity to the biggest
# sorted to avoid altering the original objects list
objectsBySize = sorted( OBJECTS, key = lambda x: x[ 1 ] )

print( objectsBySize )

# Save the resolved subproblems
# Most value per size
optimizedSizes = {}

# Assume the best case where the object is the most valuable on its size
for obj in objectsBySize:
    optimizedSizes[ obj[ 1 ] ] = {
        "value": obj[ 0 ],
        "items": [ obj ],
        "weight": obj[ 1 ]
    }
print( optimizedSizes )


for obj in objectsBySize:
    keys = [ *optimizedSizes.keys() ]
    for ii in keys:
        if obj in optimizedSizes[ ii ][ "items" ]:
            continue

        newList = {
            "value": optimizedSizes[ ii ][ "value" ] + obj[ 0 ],
            "items": optimizedSizes[ ii ][ "items" ] + [ obj ],
            "weight": optimizedSizes[ ii ][ "weight" ] + obj[ 1 ]
        }

        if newList[ "weight" ] <= CAPACITY \
            and (
                newList[ "weight" ] not in optimizedSizes \
                or newList[ "value" ] > optimizedSizes[ newList[ "weight" ] ][ "value" ]
            ):
            optimizedSizes[ newList[ "weight" ] ] = newList

sortedIndexes = sorted( optimizedSizes, key = lambda x: optimizedSizes[ x ][ "value" ] )
for idx in sortedIndexes:
    print( optimizedSizes[ idx ] )
