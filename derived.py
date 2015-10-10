from model import Game, Deck, Player

__author__ = 'Minghao'


class NormalGame(Game):
    def __init__(self):
        super(NormalGame, self).__init__()
        # do something here.

    def compare_set(self, set1, set2):
        pass


class HeartsGame(Game):
    def ___init__(self):
        super(self, NormalGame).__init__()
        # Also do something here.


class IncompleteDeck(Deck):
    """
    A deck without jokers.
    """
    def __init__(self):
        super(IncompleteDeck, self).__init__()
        # Clear the jokers list and remove jokers from deck.
        self.jokers = list()
        del self.cards[53]
        del self.cards[52]


class ComputerPlayer(Player):
    pass


class NormalGameComPlayer(ComputerPlayer):
    pass


class HeartGameComPlayer(ComputerPlayer):
    pass


class UPLevelGameComPlayer(ComputerPlayer):
    pass


class HumanPlayer(Player):
    def make_turn(self, current_set):
        isValidChoice = False
        while not isValidChoice:
            indices = list()
            hasInvalid = False
            userInput = raw_input("Enter a sequence of cards, separated by commas.")
            cards = userInput.split(",")
            for card in cards:
                try:
                    index = int(card)
                except ValueError:
                    hasInvalid = True
            if hasInvalid:
                print "The input you entered is not valid."
            else:
                isValidChoice = True

        isOkayChoice = self.validate_choice(indices, current_set)

    def validate_choice(self, choices, current_set):
        return False
    pass


class NormalHumanPlayer(HumanPlayer):
    def validate_choice(self, choices, current_set):
        pass
    pass


class HeartsHumanPlayer(HumanPlayer):
    def validate_choice(self, choices, current_set):
        pass
    pass


class UPLevelHumanPlayer(HumanPlayer):
    def validate_choice(self, choices, current_set):
        pass
    pass