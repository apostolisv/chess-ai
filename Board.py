from ChessPiece import *


class Board:

    def __init__(self, game_mode = 0):    # game_mode = 0 : player has white pieces
        self.board = []
        self.game_mode = game_mode
        for i in range(8):
            self.board.append(['empty_block' for i in range(8)])

    def place_pieces(self):
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

    def set_positions(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != 'empty_block':
                    self.board[i][j].set_position(i, j, False)

    def __getitem__(self, item):
        return self.board[item]

    def has_opponent(self, piece, x, y):
        if self.board[x][y] != 'empty_block':
            return piece.color != self.board[x][y].color
        return False

    def has_friend(self, piece, x, y):
        if self.board[x][y] != 'empty_block':
            return piece.color == self.board[x][y].color
        return False

    def has_empty_block(self, x, y):
        return self.board[x][y] == 'empty_block'

    def __repr__(self):
        return str(self.board[::-1]).replace('], ', ']\n')
