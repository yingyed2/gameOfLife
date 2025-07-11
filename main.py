from board import initBoard, printBoard, select

def main():
    board = initBoard()
    printBoard(board)
    select(board)
    printBoard(board)

if __name__ == "__main__":
    main()

