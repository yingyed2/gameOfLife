from board import BoardState, initBoard, printBoard, select, empty, reset
from game import applyRules

def main():
    boardState = BoardState() # instance
    boardState.board = initBoard()
    printBoard(boardState.board)
    select(boardState.board)
    printBoard(boardState.board)

    generation = 0  # Generation counter

    while True:
        userInput = input("Press 'Enter' to continue, 'undo', 'reset', or 'quit': \n")

        if userInput == "":
            boardState.saveState() # saves the current board
            boardState.board = applyRules(boardState.board)
            generation += 1 # incrementing
            print(f"Generation: {generation}")
            printBoard(boardState.board)

            if empty(boardState.board):
                print("No live cells. Game over!\n")
                replay = input("Would you like to replay? (yes/no): \n").lower()

                if replay == "yes":
                    reset(boardState)
                    printBoard(boardState.board)
                    select(boardState.board)
                    printBoard(boardState.board)
                    generation = 0
                else:
                    print("Exiting...")
                    break

        elif userInput.lower() == "undo":
            if boardState.undo():
                generation -= 1 # decrementing
                print(f"Undo successful. Generation: {generation}")
                printBoard(boardState.board)
            else:
                print("No previous states to undo.")

        elif userInput.lower() == "reset":
            reset(boardState)
            printBoard(boardState.board)
            select(boardState.board)
            printBoard(boardState.board)
            generation = 0

        elif userInput.lower() == "quit":
            print("Exiting...")
            break

        else:
            print("Invalid input. Press 'Enter' to continue, type 'undo', 'reset', or 'quit'.")

if __name__ == "__main__":
    main()

