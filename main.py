
import graphics
from Board import *


if __name__ == '__main__':
    board = Board()
    board.place_pieces()
    graphics.initialize()
    graphics.draw_background(board)
    graphics.start(board)


