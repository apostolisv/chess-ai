from abc import ABC


class ChessPiece(ABC):

    eatenPieces = []
    moveHistory = []
    __x_ = 0
    __y_ = 0

    def __init__(self, color):
        self.moved = False
        self.color = color

    def filter_moves(self):
        return

    def get_last_eaten(self):
        return self.eatenPieces.pop()

    def set_last_eaten(self, piece):
        self.eatenPieces.append(piece)

    def x(self):
        return self.__x_

    def y(self):
        return self.__y_

    def set_moved_previous(self):
        self.moved = self.moveHistory.pop()

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__, self.color)


class Bishop(ChessPiece):

    def get_moves(self):
        pass


class Rook(ChessPiece):

    def get_moves(self):
        pass


class Queen(ChessPiece):

    def get_moves(self):
        pass


class King(ChessPiece):

    def get_moves(self):
        pass


class Pawn(ChessPiece):
    def get_moves(self):
        pass


class Knight(ChessPiece):

    def get_moves(self):
        pass
