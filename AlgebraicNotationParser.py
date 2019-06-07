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
        northern_limit, southern_limit, eastern_limit, western_limit = 9, 0, 'i', '`'
        northern_limit_piece = data_model.ray_cast(move.piece, "N")
        southern_limit_piece = data_model.ray_cast(move.piece, "S")
        eastern_limit_piece = data_model.ray_cast(move.piece, "E")
        western_limit_piece = data_model.ray_cast(move.piece, "W")
        if northern_limit_piece:
            if northern_limit_piece.get_color() != move.piece.get_color():
                northern_limit = northern_limit_piece.get_file() + 1
            else:
                northern_limit = northern_limit_piece.get_file()
        if southern_limit_piece:
            if southern_limit_piece.get_color() != move.piece.get_color():
                southern_limit = southern_limit_piece.get_file - 1
            else:
                southern_limit = southern_limit_piece.get_file()
        if western_limit_piece:
            if western_limit_piece.get_color() != move.piece.get_color():
                western_limit = chr(ord(western_limit_piece.get_rank()) - 1)
            else:
                western_limit = western_limit_piece.get_rank()
        if eastern_limit_piece:
            if eastern_limit_piece.get_color() != move.piece.get_color():
                eastern_limit = chr(ord(eastern_limit_piece.get_rank()) + 1)
            else:
                eastern_limit = eastern_limit_piece.get_rank()
        if abs(move.get_file() - move.piece.get_file()) == 0 or abs(ord(move.get_rank()) - ord(move.piece.get_rank())) == 0:
            if move.get_file() < northern_limit and move.get_file() > southern_limit and move.get_rank() < eastern_limit and move.get_rank() > western_limit:
                return True
    elif move.piece.get_type() == "bishop":
        nw_limit, ne_limit, se_limit, sw_limit = ('`', 9), ('i', 9), ('i', 0), ('`', 0)
        nw_limit_piece = data_model.ray_cast(move.piece, "NW")
        print(nw_limit_piece)
        ne_limit_piece = data_model.ray_cast(move.piece, "NE")
        se_limit_piece = data_model.ray_cast(move.piece, "SE")
        sw_limit_piece = data_model.ray_cast(move.piece, "SW")
        if nw_limit_piece:
            if nw_limit_piece.get_color() != move.piece.get_color():
                nw_limit = chr(ord(nw_limit_piece.get_rank()) - 1), nw_limit_piece.get_file() + 1
            else:
                nw_limit = nw_limit_piece.get_rank(), nw_limit_piece.get_file()
        if ne_limit_piece:
            if ne_limit_piece.get_color() != move.piece.get_color():
                ne_limit = chr(ord(ne_limit_piece.get_rank()) + 1), ne_limit_piece.get_file() + 1
            else:
                ne_limit = ne_limit_piece.get_rank(), ne_limit_piece.get_file()
        if se_limit_piece:
            if se_limit_piece.get_color() != move.piece.get_color():
                se_limit = chr(ord(se_limit_piece.get_rank()) + 1), se_limit_piece.get_file() - 1
            else:
                se_limit = se_limit_piece.get_rank(), se_limit_piece.get_file()
        if sw_limit_piece:
            if sw_limit_piece.get_color() != move.piece.get_color():
                sw_limit = chr(ord(sw_limit_piece.get_rank()) - 1), sw_limit_piece.get_file() - 1
            else:
                sw_limit = sw_limit_piece.get_rank(), sw_limit_piece.get_file()
        print(nw_limit, ne_limit, se_limit, sw_limit)
        pos = (move.get_rank(), move.get_file())
        if move.get_file() - move.piece.get_file() == -1 * (ord(move.get_rank()) - ord(move.piece.get_rank())):
            if (pos[0] > nw_limit[0] and pos[1] < nw_limit[1]) and (pos[0] < se_limit[0] and pos[1] > se_limit[1]):
                return True
        elif move.get_file() - move.piece.get_file() == (ord(move.get_rank()) - ord(move.piece.get_rank())):
            if (pos[0] < ne_limit[0] and pos[1] < ne_limit[1]) and (pos[0] > sw_limit[0] and pos[1] > sw_limit[1]):
                return True
    elif move.piece.get_type() == "queen":
        pass
    elif move.piece.get_type() == "king":
        #TODO castling
        pass

