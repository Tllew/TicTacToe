from game import *
from player import *

def main():
    winner = False
    players = []
    wantinput = True
    print("Beginning Tic Tac Toe 2.0\n**********************\n")
    while (wantinput):
        name = input("Enter player Name\n")
        icon = input("Enter player Icon\n")
        wantinput = input("Add Player? (y/n)\n") == "y"
        players.append(Player(name, icon))
    width = int(input("Enter board width\n"))
    height = int(input("Enter board height\n"))
    game = XO(width,height)
    while(not winner):
        for player in players:
            row = int(input("Enter Column to hit!\n"))
            game.hit(row, player.icon)
            print(game.print_board())
            if game.check_win():
                print("%s has Won!!!"%player.name)
                winner = True
                if input("Play again?(y/n)") == "y":
                    main()


if __name__ == '__main__':
    main()