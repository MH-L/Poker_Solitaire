from model import Game, Deck

__author__ = 'Minghao'


class NormalGame(Game):
    def __init__(self):
        super(self, NormalGame).__init__()
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