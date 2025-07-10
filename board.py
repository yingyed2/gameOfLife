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
        # Prompt the user for input
        user_input = input("Enter row and column (e.g., 1 2): ")

        # Check if the user wants to finish
        if user_input.lower() == 'done':
            print("Selection complete.\n")
            break

        # Try to parse the input
        try:
            # Split the input into row and column
            row, col = user_input.split()
            row = int(row)
            col = int(col)

            # Validate the coordinates
            if 0 <= row < len(board) and 0 <= col < len(board[0]):
                # Set the specified cell to alive
                board[row][col] = 1
                print(f"Cell ({row}, {col}) is alive.")
            else:
                print("Invalid coordinates.")

        except ValueError:
            # Handle invalid input
            print("Invalid input. Please enter two integers separated by a space.")