import pygame
from Sprite import Sprite
from Sprite import ChessBoard
from ChessDataModel import ChessDataModel
import AlgebraicNotationParser
from ChessMove import ChessMove
import itertools

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
NUMBERS = range(1, 8)

def refresh_screen():
    screen.fill((0, 0, 0))
    chessboard.render()
    for piece in datamodel.get_pieces():
        piece.blit()
    chessboard.render_highlights()

    pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((577, 577))

chessboard = ChessBoard(screen, 577, 577, (0, 0), 'chessboard.jpg')
datamodel = ChessDataModel(screen)

turn = 'white'
selected = None
refresh_screen()

while True:
    events = pygame.event.get()
    pos = pygame.mouse.get_pos()
    if len(events) > 0:
        for event in events:
            # X BUTTON
            if event.type == pygame.QUIT:
                exit()
            # LEFT CLICK
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                rank, file = chessboard.rank_file_from_pos(pos)
                if datamodel.piece_at(rank, file) and datamodel.piece_at(rank, file).get_color() == turn:
                    chessboard.clear_highlights()
                    for spot in list(itertools.product(LETTERS, NUMBERS)):
                        move = ChessMove(datamodel.piece_at(rank, file), spot[0], spot[1])
                        if AlgebraicNotationParser.is_valid_move(move, datamodel):
                            chessboard.set_highlighted(spot[0], spot[1])
                    selected = datamodel.piece_at(rank, file)
                    print(selected)
                if selected and not datamodel.piece_at(rank, file):
                    move = ChessMove(selected, rank, file)
                    chessboard.clear_highlights()
                    if AlgebraicNotationParser.is_valid_move(move, datamodel):
                        target_piece = datamodel.get_piece(selected)
                        target_piece.set_position(rank, file)
                        print(target_piece)
                refresh_screen()
