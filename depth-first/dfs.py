# Depth First Search

from graphs_data import nodes
from graphs_data import edges

# Create the reference of every nodes children
edgesByNode = {}
for edge in edges:
    if edge[ 0 ] not in edgesByNode:
        edgesByNode[ edge[ 0 ] ] = [ edge[ 1 ] ]
    else:
        edgesByNode[ edge[ 0 ] ].append( edge[ 1 ] )

# Find the connected graphs
graphs = list()

def getGraph( rootNode ):
  graph = list()
  stack = [ rootNode ]
  while len( stack ):
    node = stack.pop( 0 )
    graph.append( node )
    if( node in edgesByNode ):
      stack[ :0 ] = edgesByNode.pop( node )

  return graph

# Print all the nodes in the provided graph
while len( edgesByNode ):
  node = list( edgesByNode.keys() )[ 0 ]
  graphs.append( getGraph( node ) )

print( graphs )
