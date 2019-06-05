import pygame
from Sprite import Sprite
from Sprite import ChessBoard
from ChessDataModel import ChessDataModel
import AlgebraicNotationParser
from ChessMove import ChessMove
import itertools

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
NUMBERS = range(0, 8)

def refresh_screen():
    screen.fill((0, 0, 0))
    chessboard.render()
    for piece in datamodel.get_pieces():
        piece.blit()
    pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((577, 577))

chessboard = ChessBoard(screen, 577, 577, (0, 0), 'chessboard.jpg')
datamodel = ChessDataModel(screen)

turn = 'white'

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
                if datamodel.piece_at(rank, file):
                    for spot in list(itertools.product(LETTERS, NUMBERS)):
                        move = ChessMove(datamodel.piece_at(rank, file), rank, file)
                        if AlgebraicNotationParser.is_valid_move(move, datamodel):
                            print(spot)
                            chessboard.set_highlighted(spot[0], spot[1])
                print(rank, file)
    refresh_screen()
