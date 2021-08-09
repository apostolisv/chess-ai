import graphics
from Board import *


if __name__ == '__main__':
    board = Board(game_mode=0)  # game_mode = 0: player has whites / 1: blacks
    board.place_pieces()
    graphics.initialize()
    graphics.draw_background(board)
    result = graphics.start(board)
    if result == 0:             # white wins
        if board.game_mode == 0:
            print('YOU WIN!')
        else:
            print('YOU LOSE!')
    elif result == 1:           # black wins
        if board.game_mode == 1:
            print('YOU WIN!')
        else:
            print('YOU LOSE!')
    elif result == 2:           # draw
        print('DRAW!')

