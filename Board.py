from ChessPiece import *


class Board:
    def __init__(self):
        self.board = []
        for i in range(8):
            self.board.append(['-' for i in range(8)])

    def place_pieces(self, player_has_whites=True):
        for j in range(8):
            self.board[1][j] = Pawn('white')
            self.board[6][j] = Pawn('black')
        self.board[0][0] = Rook('white')
        self.board[0][7] = Rook('white')
        self.board[0][1] = Knight('white')
        self.board[0][6] = Knight('white')
        self.board[0][2] = Bishop('white')
        self.board[0][5] = Bishop('white')
        self.board[0][3] = Queen('white')
        self.board[0][4] = King('white')
        self.board[7][0] = Rook('black')
        self.board[7][7] = Rook('black')
        self.board[7][1] = Knight('black')
        self.board[7][6] = Knight('black')
        self.board[7][2] = Bishop('black')
        self.board[7][5] = Bishop('black')
        self.board[7][3] = Queen('black')
        self.board[7][4] = King('black')
        if not player_has_whites:
            self.board = self.board[::-1]

    def make_move(self, x, y):
        pass

    def unmake_move(self, piece):
        pass

    def reverse_board(self):
        pass

    def __repr__(self):
        return str(self.board[::-1]).replace('], ', ']\n')
