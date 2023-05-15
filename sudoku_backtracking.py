# Solving Sudoku using BackTracking
# initialSudoku = [   [ 5, 0, 0,  9, 1, 3,  7, 2, 0 ],
#                     [ 3, 0, 0,  0, 8, 0,  5, 0, 9 ],
#                     [ 0, 9, 0,  2, 5, 0,  0, 8, 0 ],

#                     [ 6, 8, 0,  4, 7, 0,  2, 3, 0 ],
#                     [ 0, 0, 9,  5, 0, 0,  4, 6, 0 ],
#                     [ 7, 0, 4,  0, 0, 0,  0, 0, 5 ],

#                     [ 0, 2, 0,  0, 0, 0,  0, 0, 0 ],
#                     [ 4, 0, 0,  8, 9, 1,  6, 0, 0 ],
#                     [ 8, 5, 0,  7, 2, 0,  0, 0, 3 ] ]

initialSudoku = [   [ 6, 9, 0,  0, 0, 0,  7, 0, 0 ],
                    [ 0, 0, 0,  0, 9, 6,  0, 0, 0 ],
                    [ 0, 8, 0,  7, 5, 3,  0, 9, 0 ],

                    [ 0, 2, 0,  3, 7, 4,  5, 6, 1 ],
                    [ 3, 6, 0,  0, 0, 5,  0, 2, 0 ],
                    [ 0, 0, 0,  9, 6, 0,  3, 7, 8 ],

                    [ 0, 0, 6,  0, 3, 1,  0, 8, 4 ],
                    [ 0, 4, 5,  8, 0, 7,  6, 0, 0 ],
                    [ 0, 0, 0,  0, 0, 0,  0, 5, 7 ] ]

DIMENSION_SIZE = 9
GRID_SIZE = 3

def getAvailableCell( sudoku ):
    for row in range( DIMENSION_SIZE ):
        for col in range( DIMENSION_SIZE ):
            if sudoku[ row ][ col ] == 0:
                return ( row, col )
    return ( -1, -1 )

def isValidInRow( sudoku, candidate, row ):
    for col in range( DIMENSION_SIZE ):
        # print( sudoku[ row ][ col ] )
        if candidate == sudoku[ row ][ col ]:
            return False
    return True

def isValidInCol( sudoku, candidate, col ):
    for row in range( DIMENSION_SIZE ):
        # print( sudoku[ row ][ col ] )
        if candidate == sudoku[ row ][ col ]:
            return False
    return True

def isValidInGrid( sudoku, candidate, row, col ):
    # Get the first position of the grid (top - left)
    # where the candidate is located
    gridRowOffset = ( row // GRID_SIZE ) * GRID_SIZE
    gridColOffset = ( col // GRID_SIZE ) * GRID_SIZE

    for row in range( GRID_SIZE ):
        for col in range( GRID_SIZE ):
            # print( sudoku[ gridRowOffset + row ][ gridColOffset + col ] )
            if candidate == sudoku[ gridRowOffset + row ][ gridColOffset + col ]:
                return False
    return True

def isValid( sudoku, candidateNumber, row, col ):
    return (    isValidInRow( sudoku, candidateNumber, row )
            and isValidInCol( sudoku, candidateNumber, col )
            and isValidInGrid( sudoku, candidateNumber, row, col ) )


def printSudoku( sudoku ):
    for col in range( DIMENSION_SIZE ):
        if 0 not in sudoku[ col ]:
            print( sudoku[ col ] )

def solveSudoku( sudoku ):
    row, col = getAvailableCell( sudoku )
    # print( row, col )
    if row == -1:
        # print( 'done' )
        printSudoku( sudoku )
        return True

    for num in range( 1, 10 ):
        if isValid( sudoku, num, row, col ):
            # print( 'valid', num  )
            sudoku[ row ][ col ] = num
            if solveSudoku( sudoku ):
                return True

            sudoku[ row ][ col ] = 0


if __name__ == '__main__':
    solveSudoku( initialSudoku )
