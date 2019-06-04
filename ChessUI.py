import pygame
from Sprite import Sprite
from Sprite import ChessPiece

pygame.init()
screen = pygame.display.set_mode((577, 577))

chessboard = Sprite(screen, 577, 577, (0, 0), 'chessboard.jpg')
chessboard.blit()
pieces = [ChessPiece(screen, 'white', 'Pawn', 'a', 2),
          ChessPiece(screen, 'white', 'Pawn', 'b', 2),
          ChessPiece(screen, 'white', 'Pawn', 'c', 2),
          ChessPiece(screen, 'white', 'Pawn', 'd', 2),
          ChessPiece(screen, 'white', 'Pawn', 'e', 2),
          ChessPiece(screen, 'white', 'Pawn', 'f', 2),
          ChessPiece(screen, 'white', 'Pawn', 'g', 2),
          ChessPiece(screen, 'white', 'Pawn', 'h', 2),
          ChessPiece(screen, 'white', 'Rook', 'a', 1),
          ChessPiece(screen, 'white', 'Rook', 'h', 1),
          ChessPiece(screen, 'white', 'Knight', 'b', 1),
          ChessPiece(screen, 'white', 'Knight', 'g', 1),
          ChessPiece(screen, 'white', 'Bishop', 'c', 1),
          ChessPiece(screen, 'white', 'Bishop', 'f', 1),
          ChessPiece(screen, 'white', 'Queen', 'd', 1),
          ChessPiece(screen, 'white', 'King', 'e', 1),
          ChessPiece(screen, 'black', 'Pawn', 'a', 7),
          ChessPiece(screen, 'black', 'Pawn', 'b', 7),
          ChessPiece(screen, 'black', 'Pawn', 'c', 7),
          ChessPiece(screen, 'black', 'Pawn', 'd', 7),
          ChessPiece(screen, 'black', 'Pawn', 'e', 7),
          ChessPiece(screen, 'black', 'Pawn', 'f', 7),
          ChessPiece(screen, 'black', 'Pawn', 'g', 7),
          ChessPiece(screen, 'black', 'Pawn', 'h', 7),
          ChessPiece(screen, 'black', 'Rook', 'a', 8),
          ChessPiece(screen, 'black', 'Rook', 'h', 8),
          ChessPiece(screen, 'black', 'Knight', 'b', 8),
          ChessPiece(screen, 'black', 'Knight', 'g', 8),
          ChessPiece(screen, 'black', 'Bishop', 'c', 8),
          ChessPiece(screen, 'black', 'Bishop', 'f', 8),
          ChessPiece(screen, 'black', 'Queen', 'd', 8),
          ChessPiece(screen, 'black', 'King', 'e', 8),
          ]

for piece in pieces:
    piece.blit()

# pygame.draw.rect(screen, (255,0,0), (28, 28, 520, 520), 1)
pygame.display.flip()

while True:
    events = pygame.event.get()
    if len(events) > 0:
        # print(events)
        for event in events:
            # X BUTTON
            if event.type == pygame.QUIT:
                exit()
            # LEFT CLICK
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pass
