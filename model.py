__author__ = 'Minghao'

import urllib


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
        self.suite = suite
        self.rank = rank

    def compare(self, poker):
        if self.suite == 0:
            if poker.suite != 0:
                return True
            else:
                if poker.rank == 1:
                    return False
                else:
                    return True
        elif self.rank > poker.rank:
            return True
        elif self.rank < poker.rank:
            return False
        else:
            return self.rank < poker.rank

    def compare_with_theme(self, poker, theme):
        """
        Compares the poker when the first hand in the round is defined.
        theme: the suite of the first hand.
        """
        if theme == 1:
            return ()
        elif theme == 2:
            pass
        elif theme == 3:
            pass
        else:
            pass
        pass

    def compare_with_main(self, poker, main):
        """
        Compare the poker when the main suite is defined.
        main: the main suite
        """
        pass


class Deck(object):
    """
    Defines a set of poker. Singleton.
    """
    def __init__(self):
        self.spade = list()
        self.heart = list()
        self.diamond = list()
        self.club = list()
        self.jokers = [Poker(1,0), Poker(2,0)]
        for i in xrange(13):
            self.spade.append(Poker(i+1, 1))
            self.heart.append(Poker(i+1, 2))
            self.diamond.append(Poker(i+1, 3))
            self.club.append(Poker(i+1, 4))

    def shuffle(self):
        pass

    def distribute_card(self):
        pass


class Player(object):
    def __init__(self, turn):
        """
        Initializes a player of a poker game.
        :param turn: The position the player is at.
        :return: Constructor.
        """
        self.pokers = list()
        self.turn = turn


class Game(object):
    def __init__(self):
        pass

    pass


class NormalGame(Game):
    def __init__(self, game_mode):
        pass


