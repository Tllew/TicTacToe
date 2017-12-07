from game import *
from player import *

def main():
    winner = False
    players = []
    wantinput = True
    print("Beginning Tic Tac Toe 2.0\n**********************\n")
    while (wantinput):
        name = str(input("Enter player Name\n"))
        icon = str(input("Enter player Icon\n"))
        wantinput = str(input("Add Player? (y/n)\n")) == "y"
        players.append(Player(name, icon))
    width = int(input("Enter board width\n"))
    height = int(input("Enter board height\n"))
    game = XO(width,height)
    while(not winner):
        for player in players:
            row = int(input("%s Enter Column to hit!\n"%player.name))
            game.hit(row, player.icon)
            print(game.print_board())
            if game.check_win():
                print("%s has Won!!!"%player.name)
                winner = True
                if str(input("Play again?(y/n)")) == "y":
                    main()


if __name__ == '__main__':
    main()