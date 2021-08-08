import math

from ChessPiece import *
import random


ai_depth = 3


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
                            data[0].append([piece, move, board.evaluate()])
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
    # total_moves = [(piece, move, move_score)]
    total_moves = minimax(board, ai_depth, -math.inf, math.inf, True, True, [[], 0])[0]
    if len(total_moves[0]) == 0:
        print('GAME OVER!')
        if board.black_won():
            if board.game_mode == 0:
                print('YOU LOSE!')
            else:
                print('YOU WIN!')
        if board.white_won():
            if board.game_mode == 0:
                print('YOU WIN!')
            else:
                print('YOU LOSE!')
        else:
            print('DRAW!')
        return False

    pieces_and_moves = [(total_moves[0][0], total_moves[0][1])]
    best_score = total_moves[0][2]

    for move in total_moves:
        if move[2] > best_score:
            pieces_and_moves.clear()
            pieces_and_moves.append((move[0], move[1]))
            best_score = move[2]
        elif move[2] == best_score:
            pieces_and_moves.append((move[0], move[1]))

    piece_and_move = random.choice(pieces_and_moves)
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
