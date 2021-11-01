import graphics
from Board import *


if __name__ == '__main__':
    board = Board(game_mode=0, ai=False, depth=3)  # game_mode == 0: whites down / 1: blacks down
    board.place_pieces()
    
    graphics.initialize()
    graphics.draw_background(board)
    result = graphics.start(board)
    if result is None:
        exit()
    elif result == 0:             
        print('WHITE WINS!')
    elif result == 1:           
        print('BLACK WINS!')
    elif result == 2:           
        print('DRAW!')
    input()
