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

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

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

# Initial empty board
my_board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

# Game loop for AI vs. AI
while not game_is_over(my_board):
    # AI plays as "X"
    select_space(my_board, minimax(my_board, True)[1], "X")
    print_board(my_board)
    if not game_is_over(my_board):
        # AI plays as "O"
        select_space(my_board, minimax(my_board, False)[1], "O")
        print_board(my_board)
