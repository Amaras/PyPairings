"""Usefull constants"""

from enum import IntEnum


class Title(IntEnum):
    NoTitle = 0
    WCM = 1
    WFM = 2
    CM = 3
    WIM = 4
    FM = 5
    WGM = 6
    IM = 7
    GM = 8


class ColourPreference(IntEnum):
    NoPreference = -10
    AbsoluteBlack = -2
    StrongBlack = -1
    Mild = 0
    StrongWhite = 1
    AbsoluteWhite = 2
