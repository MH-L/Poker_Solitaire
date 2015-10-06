__author__ = 'Minghao'

class SameCardException(Exception):
    """
    Thrown when the system attempts to comparing two same cards, or two same cards
    appear at the same time in one game.
    """
    pass

class InvalidPokerException(Exception):
    """
    Thrown when the poker has invalid rank, invalid suite or both.
    """
    def __init__(self, message):
        self.message = message
    pass
