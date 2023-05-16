class Node:
    def __init__( self, freq, value = None, left = None, right = None ):
        self.value = value
        self.freq = freq
        self.left = left
        self.right = right

def getSortedQueue( frequencies ):
    return sorted( frequencies, key = lambda x: x.freq )

def insertNode( queue, node ):
    for index, item in enumerate( queue ):
        if node.freq < item.freq:
            queue.insert( index, node )
            return
    queue.insert( len( queue ), node )

def printPreOrder( node, prefix = '' ):
    if node:
        if node.value:
            print( f'{ node.value }: { prefix }' )
        printPreOrder( node.left, prefix + '0' )
        printPreOrder( node.right, prefix + '1' )

def getHuffmanCode( frequencies ):
    root = None
    queue = getSortedQueue( frequencies )
    while len( queue ) > 0:
        n1 = queue.pop( 0 )
        n2 = queue.pop( 0 )
        newFreq = n1.freq + n2.freq
        newNode = Node( newFreq, None, n1, n2 )
        if len( queue ) > 0:
            insertNode( queue, newNode )
        else:
            root = newNode
    return root

# In case we want to reveive a string instead of the frequencies dictionary
def getFrequenciesDict( phrase ):
    frequencies = {}
    for symbol in phrase:
        if symbol in frequencies:
            frequencies[ symbol ].freq += 1
        else:
            frequencies[ symbol ] = Node( 1, symbol )
    return frequencies

if __name__ == '__main__':
    freqDict = [
        Node( 5, 'A' ),
        Node( 12, 'B' ),
        Node( 35, 'C' ),
        Node( 3, 'D' ),
        Node( 8, 'E' ),
        Node( 14, 'F' ),
        Node( 21, 'G' ),
        Node( 1, 'H' ),
        Node( 39, 'I' )
    ]
    root = getHuffmanCode( freqDict )
    printPreOrder( root )
