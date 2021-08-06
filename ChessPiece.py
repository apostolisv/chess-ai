from abc import ABC


class ChessPiece(ABC):

    eatenPieces = []
    moveHistory = []
    positionHistory = []
    x = 0
    y = 0

    def __init__(self, color):
        self.moved = False
        self.color = color
        self.type = self.__class__.__name__

    def filter_moves(self):
        return

    def get_last_eaten(self):
        return self.eatenPieces.pop()

    def set_last_eaten(self, piece):
        self.eatenPieces.append(piece)

    def set_position(self, x, y, keep_history):
        if keep_history:
            self.positionHistory.append(self.x)
            self.positionHistory.append(self.y)
            self.moveHistory.append(self.moved)
        self.x = x
        self.y = y
        self.moved = True

    def set_old_position(self):
        position_y = self.positionHistory.pop()
        position_x = self.positionHistory.pop()
        self.y = position_y
        self.x = position_x

    def set_moved_previous(self):
        self.moved = self.moveHistory.pop()

    def __repr__(self):
        return '{}: {}'.format(self.type, self.color)


class Bishop(ChessPiece):

    def get_moves(self, board):
        pass

    def get_top_right_moves(self, board):
        pass

    def get_top_left_moves(self, board):
        pass

    def get_bot_right_moves(self, board):
        pass

    def get_top_left_moves(self, board):
        pass


class Rook(ChessPiece):

    def get_moves(self, board):
        pass

    def get_top_moves(self, board):
        pass

    def get_bot_moves(self, board):
        pass

    def get_right_moves(self, board):
        pass

    def get_left_moves(self, board):
        pass


class Queen(ChessPiece):

    def get_moves(self, board):
        moves = []
        rook = Rook(self.color)
        rook.set_position(self.x, self.y, False)
        bishop = Bishop(self.color)
        bishop.set_position(self.x, self.y, False)
        moves.append(rook.get_moves(board))
        moves.append(bishop.get_moves(board))
        return moves


class King(ChessPiece):

    def get_moves(self, board):
        pass


class Pawn(ChessPiece):
    def get_moves(self, board):
        pass

    def get_top_moves(self, board):
        pass

    def get_bot_moves(self, board):
        pass


class Knight(ChessPiece):

    def get_moves(self, board):
        pass

    def get_top_moves(self, board):
        pass

    def get_bot_moves(self, board):
        pass
