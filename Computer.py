import math
from Board import Board
from ChessPiece import *
from functools import wraps
import random


log_file = 'minimax_tree.txt'


def log_tree(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        board: Board = args[0]
        if board.log:
            depth = args[1]
            write_to_file(board, depth)
        return func(*args, **kwargs)
    return wrapper


def write_to_file(board: Board, current_depth):
    if board.depth == current_depth:
        open(log_file, 'w').close()
    with open(log_file, 'a', encoding='utf-8') as f:
        for idx, row in enumerate(board.board):
            for p in row:
                if isinstance(p, ChessPiece):
                    un = p.unicode
                else:
                    un = '\u25AF'
                f.write(un)
            if idx == 4:
                f.write('\t eval: {} | depth: {}'.format(board.evaluate(), current_depth))
            f.write('\n')
        f.write("\n")


@log_tree
def minimax(board, depth, alpha, beta, max_player, save_move, data):

    if depth == 0 or board.is_terminal():
        data[1] = board.evaluate()
        return data

    if max_player:
        max_eval = -math.inf
        for i in range(8):
            for j in range(8):
                if isinstance(board[i][j], ChessPiece) and board[i][j].color != board.get_player_color():
                    piece = board[i][j]
                    moves = piece.filter_moves(piece.get_moves(board), board)
                    for move in moves:
                        board.make_move(piece, move[0], move[1], keep_history=True)
                        evaluation = minimax(board, depth - 1, alpha, beta, False, False, data)[1]
                        if save_move:
                            if evaluation >= max_eval:
                                if evaluation > data[1]:
                                    data.clear()
                                    data[1] = evaluation
                                    data[0] = [piece, move, evaluation]
                                elif evaluation == data[1]:
                                    data[0].append([piece, move, evaluation])
                        board.unmake_move(piece)
                        max_eval = max(max_eval, evaluation)
                        alpha = max(alpha, evaluation)
                        if beta <= alpha:
                            break
        return data
    else:
        min_eval = math.inf
        for i in range(8):
            for j in range(8):
                if isinstance(board[i][j], ChessPiece) and board[i][j].color == board.get_player_color():
                    piece = board[i][j]
                    moves = piece.get_moves(board)
                    for move in moves:
                        board.make_move(piece, move[0], move[1], keep_history=True)
                        evaluation = minimax(board, depth - 1, alpha, beta, True, False, data)[1]
                        board.unmake_move(piece)
                        min_eval = min(min_eval, evaluation)
                        beta = min(beta, evaluation)
                        if beta <= alpha:
                            break
        return data


def get_ai_move(board):
    moves = minimax(board, board.depth, -math.inf, math.inf, True, True, [[], 0])
    # moves = [[pawn, move, move_score], [..], [..],[..], total_score]
    if len(moves[0]) == 0:
        return False
    best_score = max(moves[0], key=lambda x: x[2])[2]
    piece_and_move = random.choice([move for move in moves[0] if move[2] == best_score])
    piece = piece_and_move[0]
    move = piece_and_move[1]
    if isinstance(piece, ChessPiece) and len(move) > 0 and isinstance(move, tuple):
        board.make_move(piece, move[0], move[1])
    return True


def get_random_move(board):
    pieces = []
    moves = []
    for i in range(8):
        for j in range(8):
            if isinstance(board[i][j], ChessPiece) and board[i][j].color != board.get_player_color():
                pieces.append(board[i][j])
    for piece in pieces[:]:
        piece_moves = piece.filter_moves(piece.get_moves(board), board)
        if len(piece_moves) == 0:
            pieces.remove(piece)
        else:
            moves.append(piece_moves)
    if len(pieces) == 0:
        return
    piece = random.choice(pieces)
    move = random.choice(moves[pieces.index(piece)])
    if isinstance(piece, ChessPiece) and len(move) > 0:
        board.make_move(piece, move[0], move[1])
