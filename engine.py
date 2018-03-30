"""Swiss pairing engine"""
from typing import List

from Player import DutchPlayer, Player


class SwissEngine:
    def __init__(self, players: List[Player], rounds):
        self.players = sorted(
            sorted(sorted(players, key=lambda p: p.name), key=lambda p: p.title), key=lambda p: p.rating, reverse=True
        )
        self._rounds = rounds
    
    @property
    def rounds(self):
        return self._rounds


class DutchEngine(SwissEngine):
    def __init__(self, players: List[DutchPlayer], rounds):
        super().__init__(players, rounds)
