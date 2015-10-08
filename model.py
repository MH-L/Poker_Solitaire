__author__ = 'Minghao'

import constants
import gameLogicExceptions

from random import randint


class Poker(object):
    """
    Defines a Poker class. Rank 0 means joker;
    rank 1 means spade, 2 means heart, 3 means diamond,
    and 4 means club.
    """
    def __init__(self, rank, suite):
        """
        Initializes a poker.
        :param rank: rank of a poker.
        :param suite: suite of a poker. As described in class doc string.
        :return: Constructor.
        """
        if not 0 <= suite <= 4:
            raise gameLogicExceptions.InvalidPokerException\
                ("Invalid suite. Suite must be from 0 to 4.")
        elif suite == 0:
            if rank != 1 and rank != 2:
                raise gameLogicExceptions.InvalidPokerException\
                    ("Invalid joker. Joker must be either big or small.")
        elif not 1 <= rank <= 13:
            raise gameLogicExceptions.InvalidPokerException\
                ("The rank of a normal suite must be between 0 and 13.")
        self.suite = suite
        self.rank = rank

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def compare(self, poker):
        """
        Do general comparison without context.
        This method does not allow indifferent results.
        :param poker: Poker to compare with.
        :return: True if self > poker, false otherwise.
        """
        if self == poker:
            raise gameLogicExceptions.SameCardException\
                ("There should not be two same cards at the same time.")
        if self.suite == 0:
            if poker.suite != 0:
                return True
            else:
                if poker.rank == 1:
                    return False
                else:
                    return True
        elif Poker.rank_greater_than(self.rank, poker.rank):
            return True
        elif Poker.rank_greater_than(poker.rank, self.rank):
            return False
        else:
            return self.suite < poker.suite

    def compare_with_theme(self, poker, theme):
        """
        Compares the poker when the first hand in the round is defined.
        theme: the suite of the first hand.
        Theme cards are always greater than any other.
        """
        if self == poker:
            raise gameLogicExceptions.SameCardException\
                ("There should not be two same cards at the same time.")
        if self.suite == theme:
            if poker.suite != theme:
                return constants.RESULT_LARGER
            elif Poker.rank_greater_than(poker.rank, self.rank):
                return constants.RESULT_SMALLER
            else:
                return constants.RESULT_LARGER
        elif poker.suite == theme:
            return constants.RESULT_SMALLER
        else:
            return constants.RESULT_INDIFFERENT

    def compare_with_main(self, poker, main, theme):
        """
        Compare the poker when the main suite is defined.
        main: the main suite
        theme: the suite of the first hand.
        """
        if self == poker:
            raise gameLogicExceptions.SameCardException\
                ("There should not be two same cards at the same time.")
        if self.suite == main:
            if poker.suite != main:
                return constants.RESULT_LARGER
            elif Poker.rank_greater_than(poker.rank, self.rank):
                return constants.RESULT_SMALLER
            else:
                return constants.RESULT_LARGER
        elif poker.suite == main:
            return constants.RESULT_SMALLER
        elif self.suite == theme:
            if poker.suite != theme:
                return constants.RESULT_LARGER
            elif Poker.rank_greater_than(poker.rank, self.rank):
                return constants.RESULT_SMALLER
            else:
                return constants.RESULT_LARGER
        elif poker.suite == theme:
            return constants.RESULT_SMALLER
        else:
            return constants.RESULT_INDIFFERENT

    @staticmethod
    def rank_greater_than(rank1, rank2):
        """
        Returns true if and only if rank1 is strictly greater than rank2.
        Aces, which have rank 1, are the largest. That is one exception and
        also the reason the helper function exists.
        """
        if rank1 == 1:
            if rank2 != 1:
                return True
            else:
                return False
        elif rank2 == 1:
            return False
        else:
            return rank1 > rank2


class Deck(object):
    """
    Defines a set of poker. (Should be) Singleton.
    """
    def __init__(self):
        self.spade = list()
        self.heart = list()
        self.diamond = list()
        self.club = list()
        self.cards = list()
        self.jokers = [Poker(1,0), Poker(2,0)]
        for i in xrange(13):
            self.spade.append(Poker(i+1, 1))
            self.heart.append(Poker(i+1, 2))
            self.diamond.append(Poker(i+1, 3))
            self.club.append(Poker(i+1, 4))
        self.cards.extend(self.spade)
        self.cards.extend(self.heart)
        self.cards.extend(self.diamond)
        self.cards.extend(self.club)
        self.cards.extend(self.jokers)

    def shuffle(self):
        substitution = list()
        while len(self.cards) > 1:
            randSeed = randint(0, len(self.cards) - 1)
            card = self.cards.pop(randSeed)
            substitution.append(card)
        substitution.append(self.cards[0])
        self.cards = substitution

    def distribute_card(self, *player):
        counter = 0
        while counter < len(self.cards):
            for p in player:
                p.receive_card(self.cards[counter])
        pass


class Player(object):
    def __init__(self, turn):
        """
        Initializes a player of a poker game.
        :param turn: The position the player is at.
        :return: Constructor.
        """
        self.poker_hand = PokerHand()
        self.turn = turn

    def receive_card(self, card):
        self.poker_hand.receive_card(card)

    def pullout_pokers(self, *cards):
        self.poker_hand.pullout_pokers(cards)


class Game(object):
    """
    This class is supposed to be a superclass of
    all poker games the project supports.
    """
    def __init__(self):
        self.deck = Deck()

    pass


class PokerSet(object):
    """
    Defines a set of pokers.
    """
    def __init__(self):
        self.cards = list()

    def compare_set(self, other):
        """
        Compares a set with the other set of poker.
        If the set is strictly larger than the other, return True;
        otherwise return False.
        :param other: The other poker set to be compared.
        """
        pass


class PokerHand(object):
    """
    Defines the set of all pokers a player has.
    """
    def __init__(self):
        self.cards = list()

    def receive_card(self, card):
        self.cards.append(card)

    def pullout_pokers(self, *cards):
        for poker in cards:
            self.cards.remove(poker)

