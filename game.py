def adjacent(board, row, col):
    rows = len(board)
    cols = len(board[0]) # all rows have the same no. of col
    live_neighbors = 0

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue # skips the cell itself
 
            neighborRow = (row + i) % rows
            neighborCol = (col + j) % cols
            live_neighbors += board[neighborRow][neighborCol] # implicitly appends live neighbors

    return live_neighbors
"""
trickiest function so far
explain the function without wrapping first
teach by example
mod acts periodically
"""

def applyRules(board):

    rows = len(board)
    cols = len(board[0])
    new_board = []

    # initializing a new board
    for row in range(rows):
        new_row = []
        for col in range(cols):
            new_row.append(0)
        new_board.append(new_row)

    for row in range(rows):
        for col in range(cols):
            live_neighbors = adjacent(board, row, col)

            if board[row][col] == 1: # alive
                if live_neighbors < 2 or live_neighbors > 3:
                    new_board[row][col] = 0 # underpopulation & overpopulation
                else:
                    new_board[row][col] = 1 # continuity
            else: # dead
                if live_neighbors == 3:
                    new_board[row][col] = 1

    return new_board
"""
applies the rules of the game to generate the next state
we don't call initBoard() to prevent unforeseen dependencies
"""
