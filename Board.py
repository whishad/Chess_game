###############################################_____Общие классы____################################################
class Color:
    Empty = 0
    Black = 1
    White = 2

class ChessMan:
    IMG = None

    def __init__(self,color):
        self.color = color

    def __repr__(self):
        return self.IMG[0  if self.color == Color.White else 1]

###############################################_____создание фигур и доски____################################################

class Pawn(ChessMan):
    IMG = ['♟','♙']
    def get_moves (self,x,y):
        posible_moves = []

        if self.color == Color.Black and y<7  and Board.get_color (x,y+1)== Color.Empty:
            posible_moves.append([x,y])


        return posible_moves



class King(ChessMan):
    IMG = ['♚','♔']

    def get_moves(self, x, y):
        posible_moves = []

        return posible_moves
    # Набросок ферзя:
class Queen(ChessMan):
    IMG = ['♛','♕']


    # Набросок ладьи:
class Rook(ChessMan):
    IMG = ['♜','♖']


    # Набросок слона:
class Bishop(ChessMan):
    IMG = ['♝','♗']

    # Набросок коня:
class  Knight(ChessMan):
    IMG = ['♞','♘']


class Board(object):
    def __init__(self):
        self.board  = [['.']*8 for _ in range(8)]

        # Черные фигуры
        self.board[0][3] = King(Color.Black)
        self.board[0][4] = Queen(Color.Black)

        self.board[0][0] = Rook(Color.Black)     # Ладьи
        self.board[0][7] = Rook(Color.Black)

        self.board[0][2] = Bishop(Color.Black)   # Cлоны
        self.board[0][5] = Bishop(Color.Black)

        self.board[0][1] = Knight(Color.Black)   # Кони
        self.board[0][6] = Knight(Color.Black)

        # Черные пешки
        for i in range(8):
            self.board[1][i]=Pawn(Color.Black)




       # Белые Фигуры
        self.board[7][3] = King(Color.White)
        self.board[7][4] = Queen(Color.White)

        self.board[7][0] = Rook(Color.White)    # Ладьи
        self.board[7][7] = Rook(Color.White)

        self.board[7][2] = Bishop(Color.White)  # Cлоны
        self.board[7][5] = Bishop(Color.White)

        self.board[7][1] = Knight(Color.White)  # Кони
        self.board[7][6] = Knight(Color.White)

        # Белые пешки циклом
        for i in range(8):
            self.board[6][i] = Pawn(Color.White)

    def __repr__(self):
        res=''
        for y in range(8):
            res+=''.join(map(str,self.board[y]))+'\n'
        return res




###############################################_____ВЫЗОВ МЕТОДОВ____################################################


obj = Board()
print(obj)
