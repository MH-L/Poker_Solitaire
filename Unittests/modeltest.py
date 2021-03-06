__author__ = 'Minghao'
from unittest import TestCase
from model import (
    Poker, Game, Player, Deck, PokerHand
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


class GameTestCase(TestCase):
    player1 = Player(1)
    player2 = Player(2)
    player3 = Player(3)
    game = Game(player1, player2, player3)

    def test_constructor(self):
        self.assertIsNone(self.game.last_turn)
        self.assertIsNone(self.game.currentSet)
        self.assertEqual(self.game.current_turn, 1)
        self.assertEqual(self.game.finished_count, 0)
        self.assertEqual(len(self.game.deck.cards), 54)

    def test_get_player_by_turn(self):
        self.assertEqual(Player(1), self.game.get_player_with_turn(1))
        self.assertEqual(Player(2), self.game.get_player_with_turn(2))
        self.assertEqual(Player(3), self.game.get_player_with_turn(3))

    def test_get_next_turn(self):
        self.assertEqual(2, self.game.get_next_turn())
        self.player2.has_finished = True
        self.assertEqual(3, self.game.get_next_turn())

    def test_get_last_finished_player(self):
        self.player1.has_finished = True
        self.player3.has_finished = True
        self.assertEqual(self.game.get_last_finished_player(), self.player2)

class NormalGameTestCase(TestCase):
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


class PlayerTestCase(TestCase):
    pass


class PokerHandTestCase(TestCase):
    poker_hand = PokerHand()

    def test_generate_poker_dict(self):
        self.poker_hand.receive_card(Poker(1,0))
        self.poker_hand.receive_card(Poker(2,0))
        self.poker_hand.receive_card(Poker(13,1))
        self.assertEqual(3, len(self.poker_hand.cards))
        poker_dict = self.poker_hand.generate_poker_dict()
        self.assertEqual(0, poker_dict[1])
        self.assertEqual(0, poker_dict[2])
        self.assertEqual(1, poker_dict[13])
        self.assertEqual(1, poker_dict["Big Joker"])
        self.assertEqual(1, poker_dict["Small Joker"])

    def test_update_poker_dict(self):
        self.poker_hand.receive_card(Poker(1,0))
        self.poker_hand.receive_card(Poker(2,2))
        self.poker_hand.receive_card(Poker(2,3))
        self.poker_hand.receive_card(Poker(13,1))
        self.poker_hand.receive_card(Poker(13,2))
        self.poker_hand.receive_card(Poker(12,1))
        self.poker_hand.receive_card(Poker(12,3))
        self.poker_hand.receive_card(Poker(11,3))
        poker_dict = self.poker_hand.generate_poker_dict()
        cards_to_pull_out = [Poker(12,1), Poker(12,3)]
        self.poker_hand.pullout_pokers(cards_to_pull_out)
        self.assertEqual(len(self.poker_hand.cards), 6)
        self.poker_hand.update_poker_dict(cards_to_pull_out, poker_dict)
        self.assertEqual(poker_dict[12], 0)
        self.assertEqual(poker_dict[13], 2)
