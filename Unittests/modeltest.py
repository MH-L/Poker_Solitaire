__author__ = 'Minghao'
from unittest import TestCase
from model import (
    Poker, Game, Player, Deck
)
from constants import (
    RESULT_LARGER, RESULT_SMALLER, RESULT_INDIFFERENT
)
from derived import (
    IncompleteDeck, NormalGame, HeartsGame
)

import gameLogicExceptions


class PokerTestCase(TestCase):
    poker1 = Poker(1, 0)
    poker2 = Poker(2, 0)
    poker3 = Poker(4, 1)
    poker4 = Poker(9, 4)
    poker5 = Poker(12, 1)
    poker6 = Poker(7, 2)

    def testCompareCards(self):
        self.assertTrue(self.poker1.compare(self.poker2))
        self.assertTrue(self.poker2.compare(self.poker5))
        self.assertTrue(self.poker5.compare(self.poker4))
        self.assertFalse(self.poker3.compare(self.poker5))
        self.assertFalse(self.poker5.compare(self.poker1))
        self.assertFalse(self.poker5.compare(self.poker2))
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
        self.assertEqual(self.poker1.compare_with_theme(self.poker2, 1), RESULT_LARGER)
        self.assertEqual(self.poker3.compare_with_theme(self.poker4, 1), RESULT_LARGER)
        self.assertEqual(self.poker3.compare_with_theme(self.poker5, 2), RESULT_INDIFFERENT)
        self.assertEqual(self.poker4.compare_with_theme(self.poker6, 2), RESULT_SMALLER)

    def testCompareWithMain(self):
        self.assertEqual(self.poker1.compare_with_main(self.poker3, 1, 2), RESULT_LARGER)
        self.assertEqual(self.poker1.compare_with_main(self.poker2, 1, 2), RESULT_LARGER)
        self.assertEqual(self.poker3.compare_with_main(self.poker4, 4, 1), RESULT_SMALLER)
        self.assertEqual(self.poker2.compare_with_main(self.poker1, 1, 2), RESULT_SMALLER)
        self.assertEqual(self.poker4.compare_with_main(self.poker3, 4, 1), RESULT_LARGER)
        self.assertEqual(self.poker5.compare_with_main(self.poker6, 3, 2), RESULT_SMALLER)
        self.assertEqual(self.poker6.compare_with_main(self.poker3, 1, 3), RESULT_SMALLER)
        self.assertEqual(self.poker5.compare_with_main(self.poker6, 3, 4), RESULT_INDIFFERENT)
        self.assertEqual(self.poker6.compare_with_main(self.poker4, 2, 2), RESULT_LARGER)


class DeckTestCase(TestCase):
    deck = Deck()
    incomplete = IncompleteDeck()

    def testInit(self):
        self.assertEqual(len(self.deck.cards), 54)
        self.assertEqual(len(self.incomplete.cards), 52)
        print "Rank: {}, Suite: {}".format(self.deck.cards[0].rank, self.deck.cards[0].suite)
        self.assertTrue(Poker(1, 1) == self.deck.cards[0])
        self.assertTrue(Poker(1, 1) == self.incomplete.cards[0])

    def testShuffle(self):
        self.deck.shuffle()
        self.assertEqual(len(self.deck.cards), 54)


class PlayerTestCase(TestCase):
    player = Player(2)

    def testReceiveCard(self):
        self.player.receive_card(Poker(2, 1))
        self.assertEqual(self.player.get_num_cards(), 1)
        self.player.receive_card(Poker(3, 1))
        self.assertEqual(self.player.get_num_cards(), 2)


class NormalGameTest(TestCase):
    normal_game = NormalGame()
    def test_get_main_rank(self):
        poker = list()
        poker.append(Poker(1,0))
        poker.append(Poker(7,1))
        poker.append(Poker(7,2))
        poker.append(Poker(7,3))
        self.assertEqual(self.normal_game.get_main_rank(poker), 7)
        poker.append(Poker(8,4))
        self.assertIsNone(self.normal_game.get_main_rank(poker))
        poker = list()
        poker.append(Poker(1,0))
        poker.append(Poker(2,1))
        poker.append(Poker(2,2))
        poker.append(Poker(2,3))
        self.assertEqual(self.normal_game.get_main_rank(poker), 2)
        poker.append(Poker(3,3))
        self.assertEqual(self.normal_game.get_main_rank(poker), 3)

    def test_compare_set(self):
        poker = list()
        another = list()
        poker.append(Poker(1,0))
        poker.append(Poker(3,1))
        poker.append(Poker(3,2))
        poker.append(Poker(3,3))
        another.append(Poker(4,4))
        another.append(Poker(4,2))
        another.append(Poker(4,3))
        # Check for case where the two sets have different lengths.
        self.assertFalse(self.normal_game.compare_set(another, poker))
        another.append(Poker(4,1))
        # Check no sets are greater than the one with big joker.
        self.assertFalse(self.normal_game.compare_set(another, poker))
        # Remove big joker and add small joker.
        poker.remove(Poker(1,0))
        poker.append(Poker(2,0))
        # This time the function should still return false because another does
        # not have a big joker.
        self.assertFalse(self.normal_game.compare_set(another, poker))
        another.remove(Poker(4,4))
        another.append(Poker(1,0))
        # should return true because another set has a big joker.
        self.assertTrue(self.normal_game.compare_set(another, poker))
        another.remove(Poker(4,3))
        another.append(Poker(2,2))
        # wild card -- 2 -- being added, should still return true.
        self.assertTrue(self.normal_game.compare_set(another, poker))
        another.remove(Poker(2,2))
        another.append(Poker(1,2))
        # Should return false because another has mixed ranks.
        self.assertFalse(self.normal_game.compare_set(another, poker))


class PlayerTest(TestCase):
    pass
