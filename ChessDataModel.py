from Sprite import ChessPiece


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

    def get_piece(self, target_piece):
        for piece in self.pieces:
            if piece == target_piece:
                return piece

