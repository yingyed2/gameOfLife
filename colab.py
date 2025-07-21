%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def createBoard(size, p=0.5):
    """
    Generates a random initial board for Conway's Game of Life.

    Args:
        size (int): The size of the square board (size x size).
        p (float): The probability of a cell being alive (between 0 and 1).

    Returns:
        numpy.ndarray: A 2D numpy array representing the initial board.
    """
    return np.random.choice([0, 1], size=(size, size), p=[1-p, p])


def update(board):
  rows, cols = board.shape

  newBoard = np.zeros((rows, cols), dtype=int)

  for i in range(rows):
    for j in range(cols):

      total = np.sum(board[max(0, i-1):min(rows, i+2), max(0, j-1):min(cols, j+2)]) - board[i, j]

      if board[i, j] == 1 and total in [2, 3]:
        newBoard[i, j] = 1
      elif board[i, j] == 0 and total == 3:
        newBoard[i, j] = 1

  return newBoard


def animate(board, steps = 50, interval = 100):
    fig, ax = plt.subplots()
    img = ax.imshow(board, cmap='binary')

    def updateFrame(frame):
      nonlocal board
      board = update(board)
      img.set_data(board)
      return [img]

    ani = animation.FuncAnimation(fig, updateFrame, frames=steps, interval=interval, blit=True)
    plt.show()
    return ani

def main():
  board = createBoard(5)
  anim = animate(board)

  while True:
    userInput = input("Press 'Enter' to continue or 'q' to quit: ")

    if userInput == "":
      anim.event_source.stop()
      board = update(board)
      anim = animate(board)
    elif userInput.lower() == 'q':
      break
      print("Exiting...")

if __name__ == "__main__":
  main()