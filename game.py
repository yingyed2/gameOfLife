from board import initBoard, printBoard, select

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
mod is like a clock
"""



