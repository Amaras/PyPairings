"""All tournament information"""
from typing import Iterable


class Tournament:
    def __init__(self, rounds: int, system, tie_breaks: Iterable, *, name="", place="", arbiter=""):
        self.name = name
        self.place = place
        self.arbiter = arbiter
        self._rounds = rounds
        self.system = system
        self.tie_breaks = list(tie_breaks)
    
    @property
    def rounds(self):
        return self._rounds
    
    def __repr__(self):
        response = ""
        if all((self.name, self.place, self.arbiter)):
            response += f"{self.name} in {self.place} arbiter: {self.arbiter} "
        response += f"{self.rounds} rounds, {self.system} system, tiebreaks: {', '.join(self.tie_breaks)}"
        return response
    
    def __call__(self, *args, **kwargs):
        pass
