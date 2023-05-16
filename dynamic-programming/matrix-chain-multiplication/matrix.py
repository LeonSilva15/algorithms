import math
p = [ 5, 10, 3, 12, 5, 50, 6 ]

m = []
mins = []

for i in range( len( p ) - 2 ):
    minOps = math.inf
    minIdx = 0
    m.append( [] )
    for s in range( len( p ) - 2 ):
        ops = p[ s ] * p[ s + 1] * p[ s + 2]
        m[ i ].append( ops )
        if ops < minOps:
            minOps = ops
            minIdx = s + 1

    mins.append( minOps )
    p.pop( minIdx )

print( m )
print( mins )

totalOps = 0
for ops in mins:
    totalOps += ops

print( totalOps )
