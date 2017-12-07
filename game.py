class XO(object):
    def __init__(self, width, height):
        self.width = width +1
        self.height = height +1
        self.board = {(x,y):" " for x in range(1,self.width) for y in range(1,self.height)}

    def hit(self,row,icon):
        for x in range(1,self.height):
            if self.board[(row,x)] == " ":
                self.board[(row,x)] = icon
                break

    def check_win(self):
        win = False
        for x in range(1,self.width):
            for y in range(1,self.height):
                try:
                    if self.board[(x,y)] == self.board[(x+1,y)] == self.board[(x, y+1)] == self.board[(x+1, y+1)] !=" ":
                        win = True
                except:
                    pass
        return win

    def print_board(self):
        board = ""
        for y in range(self.height-1,0, -1):
            mod = ', '
            for x in range(1,self.width):
                if x == self.width-1:
                    mod = '\n'
                board += self.board[(x,y)] + mod
        return board
