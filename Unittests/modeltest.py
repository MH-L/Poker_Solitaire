__author__ = 'Minghao'
from unittest import TestCase
from model import (
    Poker, Game, Player, Deck
)
from constants import (
    RESULT_LARGER, RESULT_SMALLER, RESULT_INDIFFERENT
)

import gameLogicExceptions


class PokerTestCase(TestCase):
    poker1 = Poker(1, 0)
    poker2 = Poker(2, 0)
    poker3 = Poker(4, 1)
    poker4 = Poker(9, 4)
    poker5 = Poker(12, 1)

    def testCompareCards(self):
        self.assertTrue(self.poker1.compare(self.poker2))
        self.assertTrue(self.poker2.compare(self.poker5))
        self.assertTrue(self.poker5.compare(self.poker4))
        self.assertFalse(self.poker3.compare(self.poker5))
        self.assertRaises(gameLogicExceptions.SameCardException,
                          Poker.compare, self.poker1, self.poker1)

    def testRankGreaterThan(self):
        rank1 = 1
        rank2 = 3
        rank3 = 5
        self.assertTrue(Poker.rank_greater_than(rank1, rank2))
        self.assertFalse(Poker.rank_greater_than(rank2, rank3))
        self.assertTrue(Poker.rank_greater_than(rank1, rank3))

    def testCompareWithTheme(self):
        theme = 1
        self.assertEqual(self.poker1.compare_with_theme(self.poker2), RESULT_LARGER)
        self.assertEqual()

    def testCompareWithMain(self):
        pass


class DeckTestCase(TestCase):
    deck = Deck()

    def testInit(self):
        self.assertEqual(len(self.deck.cards), 54)
        print "Rank: {}, Suite: {}".format(self.deck.cards[0].rank, self.deck.cards[0].suite)
        self.assertTrue(Poker(1, 1) == self.deck.cards[0])

    def testShuffle(self):
        self.deck.shuffle()
        self.assertEqual(len(self.deck.cards), 54)
