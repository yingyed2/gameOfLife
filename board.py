import copy
"""
we use the copy module to create deep copies
deep copies are important for avoiding shared references
"""


class BoardState:
    def __init__(self):
        self.board = None
        self.previousStates = []

    def saveState(self):
        self.previousStates.append(copy.deepcopy(self.board))

    def undo(self):
        if self.previousStates:
            self.board = self.previousStates.pop()
            return True
        return False
"""
LIFO behavior
"""


def reset(boardState):
    boardState.board = initBoard()
    boardState.previousStates = []
    print("Game has been reset!")
"""
resetting the game
"""


def initBoard():
    rows = 5
    cols = 5

    board = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        board.append(row)
    return board
"""
initializes the 50 x 50 map
"""


def printBoard(board):

    print("\n")

    for row in board:
        printedRow = "" 
        for cell in row:
            if cell == 1:
                printedRow += "@ "
            else:
                printedRow += "- "
        printedRow = printedRow.strip()
        print(printedRow)

    print("\n")
"""
prints the board onto the terminal
"""


def select(board):

    print("Enter the coordinates of live cells one by one.\n")
    print("Type 'done' when you are finished.\n")

    while True:

        userInput = input("Enter row and column (e.g., 1 2): ")

        if userInput.lower() == 'done':
            print("Selection complete.\n")
            break

        # .split() divides the whitespaces in the user input
        coordinates = userInput.split()
        if len(coordinates) != 2:
            print("Invalid input. Please enter exactly two numbers separated by a space.")
            continue

        rowCoor, colCoor = coordinates
        if not rowCoor.isdigit() or not colCoor.isdigit():
            print("Invalid input. Please enter two positive integers.")
            continue

        row = int(rowCoor)
        col = int(colCoor)

        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            print("Invalid. Coordinates do not exist within the board's bound.")
            continue

        board[row][col] = 1
        print(f"Cell ({row}, {col}) is alive.")
"""
allows the user to set initial conditions
"""


def empty(board):

    for row in board:
        for cell in row:
            if cell == 1:
                return False
    return True
"""
checks if the board is empty
"""