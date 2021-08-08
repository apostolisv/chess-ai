from ChessPiece import *


class Board:

    def __init__(self, game_mode=0):    # game_mode == 0 : player has white pieces
        self.board = []
        self.game_mode = game_mode
        for i in range(8):
            self.board.append(['empty-block' for i in range(8)])

    def place_pieces(self):
        for j in range(8):
            self.board[1][j] = Pawn('white', 1, j)
            self.board[6][j] = Pawn('black', 6, j)
        self.board[0][0] = Rook('white', 0, 0)
        self.board[0][7] = Rook('white', 0, 7)
        self.board[0][1] = Knight('white', 0, 1)
        self.board[0][6] = Knight('white', 0, 6)
        self.board[0][2] = Bishop('white', 0, 2)
        self.board[0][5] = Bishop('white', 0, 5)
        self.board[0][3] = Queen('white', 0, 3)
        self.board[0][4] = King('white', 0, 4)
        self.board[7][0] = Rook('black', 7, 0)
        self.board[7][7] = Rook('black', 7, 7)
        self.board[7][1] = Knight('black', 7, 1)
        self.board[7][6] = Knight('black', 7, 6)
        self.board[7][2] = Bishop('black', 7, 2)
        self.board[7][5] = Bishop('black', 7, 5)
        self.board[7][3] = Queen('black', 7, 3)
        self.board[7][4] = King('black', 7, 4)
        if self.game_mode != 0:
            self.board = self.board[::-1]

    def make_move(self, piece, x, y, keep_history=False):    # history is logged when ai searches for moves
        piece_x = piece.x
        piece_y = piece.y
        self.board[piece_x][piece_y].set_last_eaten(self.board[x][y])
        self.board[x][y] = self.board[piece_x][piece_y]
        self.board[piece_x][piece_y].set_position(x, y, keep_history)
        self.board[piece_x][piece_y] = 'empty-block'

    def unmake_move(self, piece):
        x = piece.x
        y = piece.y
        self.board[x][y].set_old_position()
        self.board[x][y].set_moved_previous()
        old_x = self.board[x][y].x
        old_y = self.board[x][y].y
        self.board[old_x][old_y] = self.board[x][y]
        self.board[x][y] = 'empty-block'

    def __getitem__(self, item):
        return self.board[item]

    def has_opponent(self, piece, x, y):
        if not self.is_valid_move(x, y):
            return False
        if isinstance(self.board[x][y], ChessPiece):
            return piece.color != self.board[x][y].color
        return False

    def has_friend(self, piece, x, y):
        if not self.is_valid_move(x, y):
            return False
        if isinstance(self.board[x][y], ChessPiece):
            return piece.color == self.board[x][y].color
        return False

    def is_valid_move(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def has_empty_block(self, x, y):
        if not self.is_valid_move(x, y):
            return False
        return not isinstance(self.board[x][y], ChessPiece)

    def __repr__(self):
        return str(self.board[::-1]).replace('], ', ']\n')
