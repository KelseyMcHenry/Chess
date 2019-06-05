class ChessMove:
    def __init__(self, piece, rank, file):
        if rank.lower() not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            raise ValueError('Rank outside the board')
        if file < 1 or file > 8:
            raise ValueError('File outside the board')
        self.piece = piece
        self.rank = rank
        self.file = file

    def get_piece(self):
        return self.piece

    def get_rank(self):
        return self.rank

    def get_file(self):
        return self.file
