__author__ = 'Minghao'
INVALID_CHOICE_CONSTANT = 0

from model import (
    Deck, Player, PokerHand, Game
)
from derived import HumanPlayer, NormalGame
import sys

def main():
    print "The Poker Game is starting."
    print "Please enter 1 for normal game, 2 for hearts game,\n" \
          "and 3 for UPLevel game."
    choice = raw_input("Please enter your choice.")
    try:
        choice = int(choice)
    except ValueError:
        choice = INVALID_CHOICE_CONSTANT
    while choice not in [1,2,3]:
        choice = raw_input("Invalid option. Please enter again.")
        try:
            choice = int(choice)
        except ValueError:
            choice = INVALID_CHOICE_CONSTANT

    if choice == 1:
        startNormalGame()
    elif choice == 2:
        startHeartGame()
    else:
        startUPLevelGame()


    sys.stdin.read(1)


def startNormalGame():
    p1 = HumanPlayer(1)
    p2 = HumanPlayer(2)
    p3 = HumanPlayer(3)
    p4 = HumanPlayer(4)
    game = NormalGame(p1, p2, p3, p4)
    game.deck.shuffle()
    game.distribute_card(big2=True)
    game.print_player_cards()
    game.process_game()


def startHeartGame():
    pass


def startUPLevelGame():
    pass

if __name__ == "__main__":
    main()
