from model import Game, Deck, Player, Poker
from gameLogicExceptions import InvalidPokerException

__author__ = 'Minghao'


class NormalGame(Game):
    def __init__(self):
        super(NormalGame, self).__init__()
        # do something here.

    @staticmethod
    def compare_set(set1, current):
        """
        returns True if set1 is larger than set2;
        false if less or equal or inapplicable.
        Pre-condition: current set is checked to be
        valid.
        """
        # TODO finish this method
        if len(set1) != len(current):
            return False
        # when one of the sets are empty then raise an exception
        if len(set1) == 0:
            raise InvalidPokerException()

        has_small_joker = False
        for card in current:
            if card.suite == 0:
                # If current set has big joker,
                # then it is impossible for another
                # set to be greater, False should be returned.
                if card.rank == 1:
                    return False
                else:
                    has_small_joker = True

        if has_small_joker:
            # check to see if set1 has big joker, since
            # current set already has small joker
            choice_okay = False
            for card in set1:
                if card.suite == 0 and card.rank == 1:
                    choice_okay = True
            if not choice_okay:
                return False

        rank_set1 = Game.get_main_rank(set1)
        rank_current = Game.get_main_rank(current)
        if rank_set1 is None:
            return False
        # Since the game is normal game, big2 should be true.
        return rank_set1 == 0 or Poker.rank_greater_than(rank_set1, rank_current, big2=True)

    @staticmethod
    def get_main_rank(choices):
        # first verify the choice is consistent
        # then use compare_set helper method to determine
        # if it is valid.
        """
        :param choices: the set of cards that needs to be validated.
        """

        # check any card that is neither 2's nor jokers
        main_rank = 0
        for card in choices:
            # if the card is not a joker, then record the card's rank.
            if not card.suite == 0:
                if main_rank == 0:
                    main_rank = card.rank
                elif main_rank != card.rank:
                    if card.rank == 2:
                        continue
                    elif main_rank == 2:
                        main_rank = card.rank
                    # invalid choice if two ranks mixed, and none of them is 2.
                    else:
                        return None

        return main_rank


class HeartsGame(Game):
    def __init__(self):
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
    def __init__(self, turn, game=None):
        """
        Initializes a computer player. Computer players must know game in order
        to make decisions.
        :param game: Current poker game.
        :return: (constructor)
        """
        super(ComputerPlayer, self).__init__(turn)
        self.poker_dict = dict()
        self.generate_poker_dict()
        # game field must be protected.
        self._game = game

    def generate_poker_dict(self):
        self.poker_dict = self.poker_hand.generate_poker_dict()

    def update_poker_dict(self, cards):
        self.poker_hand.update_poker_dict(cards, self.poker_dict)

    def pullout_pokers(self, cards):
        self.poker_hand.pullout_pokers(cards)
        self.update_poker_dict(cards)


class NormalGameComPlayer(ComputerPlayer):
    def make_turn(self, current_set):
        pass
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

        cards_to_pull_out = self.get_cards_by_indices(indices)
        return cards_to_pull_out


class NormalHumanPlayer(HumanPlayer):
    pass


class HeartsHumanPlayer(HumanPlayer):
    pass


class UPLevelHumanPlayer(HumanPlayer):
    pass