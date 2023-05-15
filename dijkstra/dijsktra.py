# Dijkstra
from graphs_data import nodes
from graphs_data import edges

def dijkstra( initialNode, targetNode ):
  # store the cheapest way to get to each node
  routes = {}
  for node in nodes:
    routes[ node ] = None

  for edge in edges:
    weight = 0
    # No route has been recorded yet
    # or the current route doesn't take to the initial node
    route = routes[ edge[ 1 ] ]
    if not route or ( route[ 'n' ] != initialNode and not routes[ route[ 'n' ] ] ):
      # n: parent node
      # w: total cost to get there
      routes[ edge[ 1 ] ] = { 'n': edge[ 0 ], 'w': edge[ 2 ][ 'weight' ] }
    else:
      node = routes[ edge[ 1 ] ][ 'n' ]
      # Navigate back to get the total cost
      if node != initialNode and routes[ node ]:
        weight += routes[ node ][ 'w' ]

  route = [ targetNode ]
  node = targetNode
  while node:
    node = routes[ node ][ 'n' ]
    route[ :0 ] = [ node ]

  return route

# Print the route
print( dijkstra( 0, 14 ) )
