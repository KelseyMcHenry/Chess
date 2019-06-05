from ChessMove import ChessMove
from Sprite import ChessPiece
"Pawn to C3"


#TODO


def is_valid_move(move, data_model):
    if move.piece.get_type() == "pawn":
        if move.piece.get_color() == "white":
            # standard move
            if move.get_file() - move.piece.get_file() == 1 and move.get_rank() == move.piece.get_rank():
                if data_model.piece_at(move.get_rank(), move.get_file()):
                    # cant move if there is a piece in the way
                    return False
                else:
                    return True
            # opening move
            if move.get_file() - move.piece.get_file() == 2 and move.get_rank() == move.piece.get_rank() and move.piece.get_file() == 2:
                if data_model.piece_at(move.piece.get_rank(), move.piece.get_file() + 1) or data_model.piece_at(move.get_rank(), move.get_file()):
                    # cant move if there is a piece in the way
                    return False
                else:
                    return True
            # capture
            if move.get_file() - move.piece.get_file() == 1 and abs(ord(move.get_rank()) - ord(move.piece.get_rank())) == 1 and data_model.piece_at(move.get_rank(), move.get_file()) and data_model.piece_at(move.get_rank(), move.get_file()).get_color() == "black":
                return True
            # all other moves
            return False
        elif move.piece.get_color() == "black":
            # standard move
            if move.get_file() - move.piece.get_file() == -1 and move.get_rank() == move.piece.get_rank():
                if data_model.piece_at(move.get_rank(), move.get_file()):
                    # cant move if there is a piece in the way
                    return False
                else:
                    return True
            # opening move
            if move.get_file() - move.piece.get_file() == -2 and move.get_rank() == move.piece.get_rank() and move.piece.get_file() == 7:
                if data_model.piece_at(move.piece.get_rank(), move.piece.get_file() - 1) or data_model.piece_at(move.get_rank(), move.get_file()):
                    # cant move if there is a piece in the way
                    return False
                else:
                    return True
            # capture
            if move.get_file() - move.piece.get_file() == -1 and abs(ord(move.get_rank()) - ord(move.piece.get_rank())) == 1 and data_model.piece_at(move.get_rank(), move.get_file()) and data_model.piece_at(move.get_rank(), move.get_file()).get_color() == "white":
                return True
            # all other moves
            return False
    elif move.piece.get_type() == "knight":
        if abs(move.get_file() - move.piece.get_file()) == 2 and abs(ord(move.get_rank()) - ord(move.piece.get_rank())) == 1:
            if data_model.piece_at(move.get_rank(), move.get_file()):
                if data_model.piece_at(move.get_rank(), move.get_file()).get_color() != move.get_piece().get_color():
                    return True
            else:
                return True
        elif abs(move.get_file() - move.piece.get_file()) == 1 and abs(ord(move.get_rank()) - ord(move.piece.get_rank())) == 2 and not data_model.piece_at(move.get_rank(), move.get_file()):
            return True
        else:
            return False
    elif move.piece.get_type() == "rook":
        if abs(move.get_file() - move.piece.get_file()) == 0 or abs(ord(move.get_rank()) - ord(move.piece.get_rank())) == 0:
            return True
