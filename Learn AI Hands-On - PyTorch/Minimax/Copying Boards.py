from tic_tac_toe import *
from copy import deepcopy

my_board = [
    ["1", "2", "X"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

# Create a deep copy of my_board
new_board = deepcopy(my_board)

# Make "O" move in the center (position 5) on the new_board
select_space(new_board, 5, "O")

# Print both boards to see if modifying new_board affects my_board
print("new_board:")
print_board(new_board)

print("my_board:")
print_board(my_board)
