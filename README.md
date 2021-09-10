# Chess AI
This a very basic chess game with an ai implementation using the minimax algorithm; built in python and pygame.

To begin the game, a player has to run the main.py file providing the game mode and the depth. The game mode must be equal to 0 or 1 and it's the color of the chosen pieces (zero for whites and one for blacks). The depth is the number of times that the computer "runs a simulation of the game".
For example, if the depth is 2 and it is the computers turn, the computer will simulate every possible move it has available, and for every one of those moves, it will also play every possible move of their opponenent. To run the simulation the computer always assumes that the player plays the move in their best interest. The return value is a list containing (piece, move) tuples with the highest score.

Board

The Board class consists of a simple 2D list to store the chess pieces and a number of required methods like make_move(), unmake_move() (which is necessary for the minimax algorithm), methods to check if the game is finished, and an evaluation method which returns the total score of the caller's pieces minus the total score of the opponent's pieces (also required for the ai).

Chess Piece

The ChessPiece class is an abstract class and it is used as a parent for every piece. It consists of a method for moves filtering (prevent illegal moves like exposing the king) and some methods to keep the previous state of the chess piece intact (required by the ai when calling unmake_move()). Every chess piece is equipped with a get_score() function that is used when evaluating the board. The scores are 10 points for the pawns, 20 for knights, 30 for bishops and rooks, 120 for the queen and 1000 for the king.

Computer

The Computer class is a static class and it is used to get a move from the computer. There is a method that returns a random move and a method that returns an ai move using the minimax alogirthm.

[Chess assets by John Pablok CC-BY-SA 3.0](https://opengameart.org/content/chess-pieces-and-board-squares)
