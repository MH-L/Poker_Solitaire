__author__ = 'Minghao'
from unittest import TestCase
from model import (
    Poker, Game, Player, Deck
)
from constants import (
    RESULT_LARGER, RESULT_SMALLER, RESULT_INDIFFERENT
)


class PokerTestCase(TestCase):
    poker1 = Poker(1,0)
    poker2 = Poker(2,0)
    poker3 = Poker(4,1)
    poker4 = Poker(9,4)
    poker5 = Poker(12,1)

    def testCompareCards(self):
        poker1 = Poker(1,0)
        poker2 = Poker(2,0)
        poker3 = Poker(4,1)
        poker4 = Poker(9,4)
        poker5 = Poker(12,1)
        self.assertEquals(poker1.compare(poker2), RESULT_LARGER)
        self.assertEquals(poker2.compare(poker5), RESULT_LARGER)
        self.assertEquals(poker5.compare(poker4), RESULT_LARGER)
        self.assertEquals(poker3.compare(poker5), RESULT_SMALLER)
        pass