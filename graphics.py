import pygame
from ChessPiece import *

dark_block = pygame.image.load('assets/JohnPablok Cburnett Chess set/128px/square brown dark_png_shadow_128px.png')
light_block = pygame.image.load('assets/JohnPablok Cburnett Chess set/128px/square brown light_png_shadow_128px.png')
dark_block = pygame.transform.scale(dark_block, (75, 75))
light_block = pygame.transform.scale(light_block, (75, 75))

whitePawn = pygame.image.load('assets/JohnPablok Cburnett Chess set/128px/w_pawn_png_shadow_128px.png')
whitePawn = pygame.transform.scale(whitePawn, (75, 75))
whiteRook = pygame.image.load('assets/JohnPablok Cburnett Chess set/128px/w_rook_png_shadow_128px.png')
whiteRook = pygame.transform.scale(whiteRook, (75, 75))
whiteBishop = pygame.image.load('assets/JohnPablok Cburnett Chess set/128px/w_bishop_png_shadow_128px.png')
whiteBishop = pygame.transform.scale(whiteBishop, (75, 75))
whiteKnight = pygame.image.load('assets/JohnPablok Cburnett Chess set/128px/w_knight_png_shadow_128px.png')
whiteKnight = pygame.transform.scale(whiteKnight, (75, 75))
whiteKing = pygame.image.load('assets/JohnPablok Cburnett Chess set/128px/w_king_png_shadow_128px.png')
whiteKing = pygame.transform.scale(whiteKing, (75, 75))
whiteQueen = pygame.image.load('assets/JohnPablok Cburnett Chess set/128px/w_queen_png_shadow_128px.png')
whiteQueen = pygame.transform.scale(whiteQueen, (75, 75))

blackPawn = pygame.image.load('assets/JohnPablok Cburnett Chess set/128px/b_pawn_png_shadow_128px.png')
blackPawn = pygame.transform.scale(blackPawn, (75, 75))
blackRook = pygame.image.load('assets/JohnPablok Cburnett Chess set/128px/b_rook_png_shadow_128px.png')
blackRook = pygame.transform.scale(blackRook, (75, 75))
blackBishop = pygame.image.load('assets/JohnPablok Cburnett Chess set/128px/b_bishop_png_shadow_128px.png')
blackBishop = pygame.transform.scale(blackBishop, (75, 75))
blackKnight = pygame.image.load('assets/JohnPablok Cburnett Chess set/128px/b_knight_png_shadow_128px.png')
blackKnight = pygame.transform.scale(blackKnight, (75, 75))
blackKing = pygame.image.load('assets/JohnPablok Cburnett Chess set/128px/b_king_png_shadow_128px.png')
blackKing = pygame.transform.scale(blackKing, (75, 75))
blackQueen = pygame.image.load('assets/JohnPablok Cburnett Chess set/128px/b_queen_png_shadow_128px.png')
blackQueen = pygame.transform.scale(blackQueen, (75, 75))

highlight_block = pygame.image.load('assets/JohnPablok Cburnett Chess set/128px/highlight_128px.png')
highlight_block = pygame.transform.scale(highlight_block, (75, 75))

screen = None


def initialize():
    global screen
    pygame.init()
    pygame.display.set_caption('Chess!')
    icon = pygame.image.load('assets/icon.png')
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((600, 600))


def draw_background(board):
    screen.fill((100, 0, 0))

    block_x = 0
    for i in range(4):
        block_y = 0
        for j in range(4):
            screen.blit(light_block, (block_x, block_y))
            screen.blit(dark_block, (block_x + 75, block_y))
            screen.blit(light_block, (block_x + 75, block_y + 75))
            screen.blit(dark_block, (block_x, block_y + 75))
            block_y += 150
        block_x += 150
    step_x = 0
    step_y = pygame.display.get_surface().get_size()[0] - 75
    for i in range(8):
        for j in range(8):
            if isinstance(board[i][j], ChessPiece):
                if board[i][j].type == 'Pawn':
                    if board[i][j].color == 'white':
                        obj = whitePawn
                    else:
                        obj = blackPawn
                elif board[i][j].type == 'Rook':
                    if board[i][j].color == 'white':
                        obj = whiteRook
                    else:
                        obj = blackRook
                elif board[i][j].type == 'Knight':
                    if board[i][j].color == 'white':
                        obj = whiteKnight
                    else:
                        obj = blackKnight
                elif board[i][j].type == 'Bishop':
                    if board[i][j].color == 'white':
                        obj = whiteBishop
                    else:
                        obj = blackBishop
                elif board[i][j].type == 'Queen':
                    if board[i][j].color == 'white':
                        obj = whiteQueen
                    else:
                        obj = blackQueen
                else:
                    if board[i][j].color == 'white':
                        obj = whiteKing
                    else:
                        obj = blackKing
                screen.blit(obj, (step_x, step_y))
            step_x += 75
        step_x = 0
        step_y -= 75
    pygame.display.update()


def start(board):
    global screen
    running = True
    visible_moves = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = 7 - pygame.mouse.get_pos()[1]//75
                y = pygame.mouse.get_pos()[0]//75
                if isinstance(board[x][y], ChessPiece):
                    moves = board[x][y].get_moves(board)
                    move_positions = []
                    dimensions = pygame.display.get_surface().get_size()
                    for move in moves:
                        move_positions.append((dimensions[0] - (8 - move[1]) * 75, dimensions[1] - move[0] * 75 - 75))
                    if visible_moves:
                        draw_background(board)
                        visible_moves = False
                    for move in move_positions:
                        visible_moves = True
                        screen.blit(highlight_block, (move[0], move[1]))
                        pygame.display.update()
