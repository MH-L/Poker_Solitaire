__author__ = 'Minghao'

class SameCardException(Exception):
    """
    Thrown when the system attempts to comparing two same cards, or two same cards
    appear at the same time in one game.
    """
    def __init__(self, message=None):
        self.message = message

class InvalidPokerException(Exception):
    """
    Thrown when the poker has invalid rank, invalid suite or both.
    """
    def __init__(self, message=None):
        self.message = message

class InvalidThemeException(Exception):
    """
    Thrown only when the theme of a round is joker.
    Theme should never be that.
    """
    def __init__(self, message=None):
        self.message = message