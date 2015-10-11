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

    def to_string(self):
        retStr = ""
        if self.suite == 0:
            if self.rank == 1:
                return "Big Joker"
            else:
                return "Small Joker"
        elif self.suite == 1:
            retStr += "Spade "
        elif self.suite == 2:
            retStr += "Heart "
        elif self.suite == 3:
            retStr += "Diamond "
        elif self.suite == 4:
            retStr += "Club "
        else:
            raise gameLogicExceptions.InvalidPokerException("Invalid card.")
        if self.rank == 1:
            retStr += "A"
        elif self.rank == 11:
            retStr += "J"
        elif self.rank == 12:
            retStr += "Q"
        elif self.rank == 13:
            retStr += "K"
        else:
            retStr += str(self.rank)
        return retStr

    def compare(self, poker, big2=False, suppress=False):
        """
        Do general comparison without context.
        This method does not allow indifferent results.
        :param poker: Poker to compare with.
        :return: True if self > poker, false otherwise.
        """
        if self == poker and not suppress:
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
        elif poker.suite == 0:
            return False
        elif Poker.rank_greater_than(self.rank, poker.rank, big2=big2):
            return True
        elif Poker.rank_greater_than(poker.rank, self.rank, big2=big2):
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
        if self.suite == 0:
            if poker.suite == 0:
                if self.rank == 1:
                    return constants.RESULT_LARGER
                else:
                    return constants.RESULT_SMALLER
            else:
                return False
        elif poker.suite == 0:
            return False
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

    def compare_with_main(self, poker, main, theme):
        """
        Compare the poker when the main suite is defined.
        main: the main suite
        theme: the suite of the first hand.
        """
        if self == poker:
            raise gameLogicExceptions.SameCardException\
                ("There should not be two same cards at the same time.")
        if self.suite == 0:
            if poker.suite != 0:
                return constants.RESULT_LARGER
            elif self.rank == 1:
                return constants.RESULT_LARGER
            else:
                return constants.RESULT_SMALLER
        elif poker.suite == 0:
            return False
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
    def rank_greater_than(rank1, rank2, big2=False):
        """
        Returns true if and only if rank1 is strictly greater than rank2.
        Aces, which have rank 1, are the largest. That is one exception and
        also the reason the helper function exists.
        """
        if big2:
            if rank1 == 2:
                if rank2 != 2:
                    return True
                else:
                    return False
            elif rank2 == 2:
                return False
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
        self.jokers = [Poker(1, 0), Poker(2, 0)]
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


class Player(object):
    def __init__(self, turn):
        """
        Initializes a player of a poker game.
        Poker hand is initially empty.
        :param turn: The position the player is at.
        :return: Constructor.
        """
        self.__poker_hand = PokerHand()
        self.turn = turn

    def receive_card(self, card):
        self.__poker_hand.receive_card(card)

    def pullout_pokers(self, *cards):
        self.__poker_hand.pullout_pokers(cards)

    def get_num_cards(self):
        return len(self.__poker_hand.cards)

    def print_cards_in_hand(self):
        print self.__poker_hand.to_string()

    def sort_hand(self, big2=False):
        self.__poker_hand.sort(big2=big2)

    def make_turn(self, current_set):
        """
        Player pullout his card. This requires support from algorithms.
        """
        pass

    def pull_out(self, indices):
        retval = list()
        for index in indices:
            retval.append(self.__poker_hand.cards[index])
        return retval


class Game(object):
    """
    This class is supposed to be a superclass of
    all poker games the project supports.
    """
    def __init__(self, *players):
        self.deck = Deck()
        self.players = players
        self.currentSet = None

    def compare_set(self, set1, set2):
        """
        Compares a set with the other set of poker.
        If the  first set is strictly larger than the second, return True;
        otherwise return False.
        :param set1: The first poker set to be compared.
        :param set2: The second poker set to be compared.
        Note: The result also depends on game type.
        """
        pass

    def validate_choice(self, choices, current_set):
        """
        Validate a player's choice. The player's choice
        is valid if and only if 1) It forms a full set of cards;
        2) The set of cards is greater than the current_set.
        """
        pass

    def distribute_card(self, big2=False):
        counter = 0
        while counter < len(self.deck.cards):
            for p in self.players:
                if counter >= len(self.deck.cards):
                    break
                p.receive_card(self.deck.cards[counter])
                counter += 1

        for p in self.players:
            p.sort_hand(big2=big2)

    def print_player_cards(self):
        for p in self.players:
            p.print_cards_in_hand()

    def process_game(self):
        pass


class PokerSet(object):
    """
    Defines a set of pokers.
    """
    def __init__(self):
        self.cards = list()


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

    def to_string(self):
        returnStr = "The list of cards are:\n"
        for card in self.cards:
            returnStr += card.to_string()
            returnStr += "\n"
        return returnStr

    def sort(self, big2=False):
        newCards = list()
        while len(self.cards) > 0:
            mini = self.cards[0]
            index = 0
            for i in range(len(self.cards)):
                if mini.compare(self.cards[i], big2=big2, suppress=True):
                    mini = self.cards[i]
                    index = i
            newCards.append(mini)
            del self.cards[index]

        self.cards = newCards

