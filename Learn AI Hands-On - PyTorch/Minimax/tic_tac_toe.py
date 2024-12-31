from tic_tac_toe import *

# Initial board setup
my_board = [
    ["1", "2", "3"],  # Empty spaces
    ["4", "5", "6"],  # Empty spaces
    ["7", "8", "9"]   # Empty spaces
]

# Print the initial board
print_board(my_board)

# Make "X" move in space 1 (top-left)
select_space(my_board, 1, "X")

# Make "O" move in space 5 (center)
select_space(my_board, 5, "O")

# Make "X" move in space 2 (top-middle)
select_space(my_board, 2, "X")

# Make "O" move in space 8 (bottom-middle)
select_space(my_board, 8, "O")

# Make "X" move in space 3 (top-right) to win the game
select_space(my_board, 3, "X")

# Print the available moves after these moves
available_moves(my_board)

# Print the board after all moves
print_board(my_board)

# Check if "X" has won
x_won = has_won(my_board, "X")
print(f"Has X won? {x_won}")

# Check if "O" has won
o_won = has_won(my_board, "O")
print(f"Has O won? {o_won}")
