from board import initBoard, printBoard, select, empty
from game import applyRules

def main():
    board = initBoard()
    printBoard(board)
    select(board)
    printBoard(board)

    while True:
        userInput = input("Press 'Enter' to continue or type 'quit' to exit: \n")

        if userInput == "":
            board = applyRules(board)
            printBoard(board)

            if empty(board):
                print("No live cells. Game over!\n")
                replay = input("Would you like to replay? (yes/no): \n").lower()

                if replay == "yes":
                    board = initBoard()
                    printBoard(board)
                    select(board)
                    printBoard(board)
                else:
                    print("Exiting...")
                    break

        elif userInput.lower() == "quit":
            print("Exiting...")
            break
        else:
            print("Invalid input. Press 'Enter' to continue or type 'quit' to exit.")

if __name__ == "__main__":
    main()

