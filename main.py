
import graphics
from Board import *


if __name__ == '__main__':
    board = Board()
    board.place_pieces()
    graphics.initialize(board)
    graphics.start(board)


