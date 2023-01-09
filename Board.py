cclass Color (object):
    Empty = 0
    Black = 1
    White = 2



class ChessMan(object):
    IMG = None

    def __init__(self,color):
        self.color = color

    def __repr__(self):
        return self.IMG[0  if self.color == Color.White else 1]



class Pawn(ChessMan):
    IMG = ['♙','♟']
    def get_moves (self,x,y):
        posible_moves = []

        if self.color == Color.Black and y<7  and Board.get_color (x,y+1)== Color.Empty:
            posible_moves.append([x,y])


        return posible_moves



class King(ChessMan):
    IMG = ['♔','♚']

    def get_moves(self, x, y):
        posible_moves = []

        return posible_moves


class Board(object):
    def __init__(self):
        self.board  = [['.']*8 for _ in range(8)]
        self.board[1][2] = Pawn(Color.Black)
        self.board[0][3] = King(Color.Black)
        self.board[7][3] = King(Color.White)

    def __repr__(self):
        res=''
        for y in range(8):
            res+=''.join(map(str,self.board[y]))+'\n'
        return res

obj = Board()

print(obj)

