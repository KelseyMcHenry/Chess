from Sprite import ChessPiece
from AlgebraicNotationParser import is_valid_move
from ChessMove import ChessMove
import itertools

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
NUMBERS = range(1, 9)


class ChessDataModel:
    def __init__(self, screen):
        self.pieces = [ChessPiece(screen, 'white', 'Pawn', 'a', 2),
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
                       ChessPiece(screen, 'black', 'King', 'e', 8)
                       ]

    def get_pieces(self):
        return self.pieces

    def piece_at(self, rank, file):
        for piece in self.pieces:
            if piece.get_rank() == rank and piece.get_file() == file:
                return piece
        return

    def pieces_in_rank(self, rank):
        return_pieces = []
        for piece in self.pieces:
            if piece.get_rank() == rank:
                return_pieces.append(piece)
        return_pieces.sort(key=lambda x: x.get_file())
        return return_pieces

    def pieces_in_file(self, file):
        return_pieces = []
        for piece in self.pieces:
            if piece.get_file() == file:
                return_pieces.append(piece)
        return_pieces.sort(key=lambda x: ord(x.get_rank()))
        return return_pieces

    def pieces_in_diagonal(self, rank, file, left_right):
        return_pieces = []
        for piece in self.pieces:
            if left_right == "left":
                if piece.get_file() - file == -1 * (ord(piece.get_rank()) - ord(rank)):
                    return_pieces.append(piece)
            if left_right == "right":
                if piece.get_file() - file == ord(piece.get_rank()) - ord(rank):
                    return_pieces.append(piece)
        return_pieces.sort(key=lambda x: ord(x.get_rank()))
        return return_pieces

    def get_piece(self, target_piece):
        for piece in self.pieces:
            if piece == target_piece:
                return piece

    def ray_cast(self, piece, direction):
        origin = piece.get_rank(), piece.get_file()
        ray_cast_pieces = []
        if direction == "N":
            pieces_in_rank = self.pieces_in_rank(origin[0])
            ray_cast_pieces = [p for p in pieces_in_rank if p.get_file() > piece.get_file()]
            ray_cast_pieces.sort(key=lambda x: x.get_file())
        elif direction == "S":
            pieces_in_rank = self.pieces_in_rank(origin[0])
            ray_cast_pieces = [p for p in pieces_in_rank if p.get_file() < piece.get_file()]
            ray_cast_pieces.sort(key=lambda x: x.get_file(), reverse=True)
        elif direction == "E":
            pieces_in_file = self.pieces_in_file(origin[1])
            ray_cast_pieces = [p for p in pieces_in_file if p.get_rank() > piece.get_rank()]
            ray_cast_pieces.sort(key=lambda x: ord(x.get_rank()))
        elif direction == "W":
            pieces_in_file = self.pieces_in_file(origin[1])
            ray_cast_pieces = [p for p in pieces_in_file if p.get_rank() < piece.get_rank()]
            ray_cast_pieces.sort(key=lambda x: ord(x.get_rank()), reverse=True)
        elif direction == "NW":
            pieces_in_file = self.pieces_in_diagonal(origin[0], origin[1], "left")
            ray_cast_pieces = [p for p in pieces_in_file if p.get_file() > piece.get_file() and p.get_rank() < piece.get_rank()]
            ray_cast_pieces.sort(key=lambda x: x.get_file())
        elif direction == "NE":
            pieces_in_file = self.pieces_in_diagonal(origin[0], origin[1], "right")
            ray_cast_pieces = [p for p in pieces_in_file if p.get_file() > piece.get_file() and p.get_rank() > piece.get_rank()]
            ray_cast_pieces.sort(key=lambda x: x.get_file())
        elif direction == "SW":
            pieces_in_file = self.pieces_in_diagonal(origin[0], origin[1], "right")
            ray_cast_pieces = [p for p in pieces_in_file if p.get_file() < piece.get_file() and p.get_rank() < piece.get_rank()]
            ray_cast_pieces.sort(key=lambda x: x.get_file(), reverse=True)
        elif direction == "SE":
            pieces_in_file = self.pieces_in_diagonal(origin[0], origin[1], "left")
            ray_cast_pieces = [p for p in pieces_in_file if p.get_file() < piece.get_file() and p.get_rank() > piece.get_rank()]
            ray_cast_pieces.sort(key=lambda x: x.get_file(), reverse=True)
        if ray_cast_pieces:
            return ray_cast_pieces[0]
        else:
            return None

    def capture(self, captured_piece):
        for piece in self.pieces:
            if piece == captured_piece:
                self.pieces.remove(piece)
                break

    def king_in_check(self, rank, file, color):
        for piece in self.get_pieces():
            if piece.get_color() != color and piece.get_type() != "king":
                if piece.get_type() != "pawn":
                    move = ChessMove(piece, rank, file)
                    if is_valid_move(move, self):
                        return True
                else:
                    if color == "white":
                        if piece.get_file() - file == 1 and abs(ord(piece.get_rank()) - ord(rank)) == 1:
                            return True
                    elif color == "black":
                        if piece.get_file() - file == -1 and abs(ord(piece.get_rank()) - ord(rank)) == 1:
                            return True
        return False

    def king_in_checkmate(self, rank, file, color):
        if self.king_in_check(rank, file, color):
            count = 0
            for spot in list(itertools.product(LETTERS, NUMBERS)):
                move = ChessMove(self.piece_at(rank, file), spot[0], spot[1])
                if is_valid_move(move, self):
                    count += 1
            if count == 0:
                return True
        return False

    # TODO King in stalemate
