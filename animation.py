%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import display, HTML # Import HTML for displaying animation

def createBoard(size):

    board = np.zeros((size, size), dtype=int)
    print(f"\nEnter coordinates of initially alive cells (between 0 and {size - 1}).") #explain the f-string (avoiding tedious concatenating)
    print("Type 'done' when you're finished.\n")

    while True:
        coords = input("Enter coordinates as 'row,col': ")
        if coords.lower() == 'done':
            break
        try:
            coords_list = coords.strip().split(',')
            if len(coords_list) == 2:
                i = int(coords_list[0])
                j = int(coords_list[1])

                if 0 <= i < size and 0 <= j < size:
                    board[i, j] = 1
                else:
                    print("Out of bounds. Try again.")
            else:
                 print("Invalid input. Format must be: row,col")
        except ValueError:
            print("Invalid input. Format must be: row,col")

    return board
"""
  Generates an empty board and allows user input to activate cells.

  Args:
      size (int): The size of the square board (size x size).

  Returns:
      numpy.ndarray: A 2D numpy array with user-specified live cells.
"""


def update(board):
    """
    Applies the rules of Conway's Game of Life to update the board.

    Args:
        board (numpy.ndarray): The current state of the board.

    Returns:
        numpy.ndarray: The next state of the board.
    """
    size = board.shape[0]
    newBoard = board.copy()

    for i in range(size):
        for j in range(size):
            # Count live neighbors
            live_neighbors = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if (x != 0 or y != 0) and (0 <= i + x < size) and (0 <= j + y < size):
                        live_neighbors += board[i + x, j + y]

            # Apply Game of Life rules
            if board[i, j] == 1:  # If the cell is alive
                if live_neighbors < 2 or live_neighbors > 3:
                    newBoard[i, j] = 0  # Cell dies
            else:  # If the cell is dead
                if live_neighbors == 3:
                    newBoard[i, j] = 1  # Cell becomes alive

    return newBoard


def animate(board, steps=100, interval=100, save_as_gif=True, filename="game_of_life.gif"):
    fig, ax = plt.subplots()
    img = ax.imshow(board, cmap='binary')
    plt.title("Conway's Game of Life")
    plt.axis('off') # Hide axes

    def updateFrame(frame):
        nonlocal board
        board = update(board)
        img.set_data(board)
        return [img]

    ani = animation.FuncAnimation(
        fig,
        updateFrame,
        frames=steps,
        interval=interval,
        blit=True,
        repeat=False
    )

    if save_as_gif:
        # Requires imagemagick or ffmpeg
        # In Colab, ffmpeg is usually available
        print(f"Saving animation to {filename}...")
        ani.save(filename, writer='pillow', fps=10) # Use pillow writer for GIF
        print("Animation saved.")
        # Optional: Display the saved GIF in the notebook
        # try:
        #     display(HTML(f'<img src="{filename}">'))
        # except Exception as e:
        #     print(f"Could not display GIF in notebook: {e}")

    plt.close(fig) # Close the figure after saving

    return ani

def main():
    size = int(input("Enter the board size: "))
    board = createBoard(size)
    # Call animate with save_as_gif=True and specify steps=100
    anim = animate(board, steps=100, save_as_gif=True)

if __name__ == "__main__":
  main()