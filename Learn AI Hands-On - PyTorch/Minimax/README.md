Imagine that we're playing a simple game like Tic-Tac-Toe. The idea behind minimax and game trees is all about looking ahead in the game to make the smartest possible move.

# What is Minimax?
Minimax is a way of thinking two steps (or more) ahead to figure out your best move. It works by imagining all the possible moves you and your opponent could make and choosing the one that gives you the best chance to win while assuming your opponent is also playing their best.

Think of it like playing a game of chess in your mind before actually moving any pieces.

# What are Game Trees?
A game tree is like a “map” of all the possible moves you and your opponent could make. Each "branch" of the tree represents a different move, and each "leaf" at the end of the branch represents a final outcome: you win, you lose, or it's a tie.


# How Does Minimax Use the Game Tree?
Imagine you're "X" in a game of Tic-Tac-Toe, and it's your turn. Here’s how minimax helps us decide what to do:

Step 1: Imagine Your Move

Let’s say you decide to place your "X" in one of the empty squares. This creates a new game state. Each possible move creates a new branch in the tree.

Step 2: Imagine Your Opponent’s Move

Now, imagine your opponent ("O") sees what you did and tries to counter your move. They’ll choose the best spot to put their "O" to try to win or block you.

Step 3: Keep Thinking Ahead

You then imagine your next move and how your opponent would respond again. This process repeats until the game ends.

# What are Leaves in the Game Tree?
A leaf is a point where the game is over. There are no more moves left because:

> Someone has won (e.g., "X" has three in a row).

> It's a tie (all squares are filled, but no one won).

> Even if there are empty squares left on the board, if someone has already won or the game is a tie, you don’t need to look ahead anymore. That’s why those game states are called “leaves.”


# Why Does Minimax Work?
Minimax assumes that both players are smart and always make the best move. By looking ahead at all possible outcomes, it chooses the move that gives you the best result, even if your opponent plays perfectly.

Example:

Minimax would consider every possible way the game could play out and decide whether placing "X" in the bottom-left corner is better than other options.

* In short minimax is like playing the entire game in your head before making a move. It helps you choose the smartest option by imagining every possibility, assuming your opponent is just as clever as you. The “leaves” in the game tree are where the game ends—no more moves to think about!

![Minimax Board](https://github.com/user-attachments/assets/9581de33-4e33-437e-bc0e-c111deb1c51d)


# tic_tac_toe.py
In the first code (tic_tac_toe.py), we set up a Tic-Tac-Toe game board and simulated moves for players "X" and "O" by selecting spaces on the board. We printed the board after each move, checked the available moves, and then checked if either "X" or "O" had won using the has_won() function.

# Detecting_Tic-Tac-Toe_Leaves.py
In the second part, we implemented functions to detect if the game is over (game_is_over()) and evaluate the board (evaluate_board()). The game_is_over() checks for a winner or a tie, and evaluate_board() returns the result based on the winner or a tie.

# Evaluating Leaves
In this scenario, the goal is to use the minimax algorithm to evaluate non-leaf nodes in a Tic-Tac-Toe game tree. The maximizing player ("X") aims to maximize the board's value, while the minimizing player ("O") tries to minimize it. At the leaf nodes, we evaluate the game outcomes (win = 1, tie = 0, loss = -1). The values are then propagated up the tree, with each non-leaf node's value depending on whether it's the maximizing or minimizing player's turn. The optimal move is chosen based on the highest value for "X" and the lowest value for "O."

# Copying Boards.py
In this code, we first created a reference to my_board by assigning new_board = my_board, meaning both variables pointed to the same board. Modifying new_board also affected my_board. Then, we used deepcopy(my_board) to create an independent copy of my_board for new_board. After making a move on new_board, we observed that my_board remained unchanged, demonstrating that deepcopy() creates a separate copy, so changes to new_board don't affect my_board.

# Minimax.py
In this code, we defined the minimax() function to evaluate possible moves for a Tic-Tac-Toe game. We loop through all available moves, create a deep copy of the current board for each move, and apply the move using select_space(). The symbol used for the move is based on whether the player is maximizing ("X") or minimizing ("O"). After making the move, we return the new board. The function is called with x_winning as the input board and the maximizing player (True).

# Recursion.py
In this code, we implemented the minimax algorithm for a Tic-Tac-Toe game. The minimax() function recursively evaluates all possible moves, determining the best move for the current player. It uses a base case to return a value when the game is over, and recursively explores future moves, maximizing for "X" and minimizing for "O". We tested the function on three boards (x_winning, o_winning, and new_game) to evaluate the best possible move for "X". The results indicate whether "X" wins, "O" wins, or if the game is a tie.

# Improved_Minimax.py
In this code, we implement the minimax algorithm to determine the best move for the player "X" (maximizing player) in a Tic-Tac-Toe game. The minimax function recursively evaluates all possible game states, considering both maximizing and minimizing players (X and O). It returns the best move and its corresponding value based on the current board state. We test the function on different game boards (x_winning, o_winning, and new_game) to see how the algorithm chooses the best move for "X" in each scenario.

# Play.py
In this code, we implemented a Tic-Tac-Toe game where two AI players (X and O) play against each other using the Minimax algorithm. The minimax() function evaluates all possible moves and selects the optimal one for each player. The game loop alternates between the two AI players, making moves based on the results from the minimax() function. The board is printed after each move to show the current game state.

# Reference:
This project implements the Minimax algorithm to create an unbeatable AI for Tic-Tac-Toe. It uses game trees to evaluate all possible moves and outcomes, enabling optimal decision-making for both players. The AI alternates between maximizing and minimizing strategies to ensure the best possible result.

Developed using resources from [Codecademy](https://www.codecademy.com).







