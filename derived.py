from model import Game, Deck, Player

__author__ = 'Minghao'


class NormalGame(Game):
    def __init__(self):
        super(NormalGame, self).__init__()
        # do something here.

    def compare_set(self, set1, set2):
        """
        returns True if set1 is larger than set2;
        false if less or equal or inapplicable.
        """
        # TODO finish this method
        if len(set1) != len(set2):
            return False
        if len(set1) == 0:
            raise
        initialRank = set1[0].rank
        for poker in set1:
            if initialRank != poker.rank:
                return False

    def validate_choice(self, choices, current_set):
        # first verify the choice is consistent
        # then use compare_set helper method to determine
        # if it is valid.

        return False


class HeartsGame(Game):
    def ___init__(self):
        super(HeartsGame, self).__init__()
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
        indices = list()
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
                    break
                if index >= self.get_num_cards():
                    hasInvalid = True
                    break
                indices.append(index)
            if hasInvalid:
                print "The input you entered is not valid."
            else:
                isValidChoice = True

        isOkayChoice = self.validate_choice(indices, current_set)

    def validate_choice(self, choices, current_set):
        return False
    pass


class NormalHumanPlayer(HumanPlayer):
    pass


class HeartsHumanPlayer(HumanPlayer):
    pass


class UPLevelHumanPlayer(HumanPlayer):
    def validate_choice(self, choices, current_set):
        pass
    pass