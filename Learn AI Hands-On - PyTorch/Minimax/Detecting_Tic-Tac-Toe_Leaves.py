# Define the boards
start_board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

x_won = [
    ["X", "O", "3"],
    ["4", "X", "O"],
    ["7", "8", "X"]
]

o_won = [
    ["O", "X", "3"],
    ["O", "X", "X"],
    ["O", "8", "9"]
]

tie = [
    ["X", "X", "O"],
    ["O", "O", "X"],
    ["X", "O", "X"]
]

# Function to check if a player has won
def has_won(board, player):
    # Check for a winner
    winning_combinations = [
        # Rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    
    # Check if any winning combination exists for the given player
    for combination in winning_combinations:
        if combination[0] == combination[1] == combination[2] == player:
            return True
    return False

# Function to check if the game is over
def game_is_over(board):
    # Check if any player has won
    if has_won(board, "X") or has_won(board, "O"):
        return True
    
    # Check if there are any empty spots left
    for row in board:
        for cell in row:
            if cell not in ["X", "O"]:  # If there's any number left, game is not over
                return False
    
    # If no winner and no empty spots, it's a tie
    return True

# Function to evaluate the board
def evaluate_board(board):
    # If "X" has won, return 1
    if has_won(board, "X"):
        return 1
    # If "O" has won, return -1
    elif has_won(board, "O"):
        return -1
    # If it's a tie, return 0
    else:
        return 0

# Test the functions on each board and print the result if the game is over
if game_is_over(start_board):
    print(f"start_board evaluation: {evaluate_board(start_board)}")  # Expected: 0 (game is ongoing)

if game_is_over(x_won):
    print(f"x_won evaluation: {evaluate_board(x_won)}")  # Expected: 1 (X won)

if game_is_over(o_won):
    print(f"o_won evaluation: {evaluate_board(o_won)}")  # Expected: -1 (O won)

if game_is_over(tie):
    print(f"tie evaluation: {evaluate_board(tie)}")  # Expected: 0 (It's a tie)
