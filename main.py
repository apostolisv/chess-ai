import graphics
from Board import *


if __name__ == '__main__':
    keep_playing = True

    board = Board(game_mode=0, ai=True, depth=1, log=True)  # game_mode == 0: whites down / 1: blacks down

    while keep_playing:
        graphics.initialize()
        board.place_pieces()
        graphics.draw_background(board)
        keep_playing = graphics.start(board)
        