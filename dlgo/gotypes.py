import enum
from collections import namedtuple

COLS = 'ABCDEFGHJKLMNOPQRST'

class Player(enum.Enum):

    black = 1
    white = 2

    @property
    def other(self):
        return Player.black if self == Player.white else Player.white

    def __str__(self):
        if self == Player.black:
            player_string = 'black'
        else:
            player_string = 'white'
        return '%s' % player_string

    __repr__ = __str__


