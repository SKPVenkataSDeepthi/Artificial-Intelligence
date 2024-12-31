from tic_tac_toe import *
from copy import deepcopy

# Function to check if the game is over
def game_is_over(board):
  return has_won(board, "X") or has_won(board, "O") or len(available_moves(board)) == 0

# Function to evaluate the board
def evaluate_board(board):
  if has_won(board, "X"):
    return 1  # X wins
  elif has_won(board, "O"):
    return -1  # O wins
  else:
    return 0  # Tie

# Sample game boards
new_game = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

x_winning = [
    ["X", "2", "O"],
    ["4", "O", "6"],
    ["7", "8", "X"]
]

o_winning = [
    ["X", "X", "O"],
    ["4", "X", "6"],
    ["7", "O", "O"]
]

# Minimax function to evaluate the best move
def minimax(input_board, is_maximizing):
  # Base case - the game is over, so we return the value of the board
  if game_is_over(input_board):
    return [evaluate_board(input_board), ""]
  
  # Initialize best_move
  best_move = ""
  
  # Maximizing player (X)
  if is_maximizing:
    best_value = -float("Inf")
    symbol = "X"
  else:
    # Minimizing player (O)
    best_value = float("Inf")
    symbol = "O"
  
  # Loop through all available moves
  for move in available_moves(input_board):
    new_board = deepcopy(input_board)
    select_space(new_board, move, symbol)
    
    # Recursive call to minimax for the next move
    hypothetical_value = minimax(new_board, not is_maximizing)[0]
    
    # Maximizing player: Choose the highest value
    if is_maximizing and hypothetical_value > best_value:
      best_value = hypothetical_value
      best_move = move  # Update the best move
    
    # Minimizing player: Choose the lowest value
    if not is_maximizing and hypothetical_value < best_value:
      best_value = hypothetical_value
      best_move = move  # Update the best move
  
  # Return the best value and the corresponding best move
  return [best_value, best_move]

# Test the minimax function on the boards
print("Result for x_winning board (X's turn):", minimax(x_winning, True))
print("Result for o_winning board (X's turn):", minimax(o_winning, True))
print("Result for new_game board (X's turn):", minimax(new_game, True))
