"""Player class: all the information available on the player"""
from typing import Iterable, List

from constants import Title, ColourPreference


class Player:
    def __init__(self, name: str, rating: int, rating_type: str, country: str, licence_id: int, birth_date,
                 tie_breaks: Iterable, title: Title = Title.NoTitle, score=0):
        self.pairing_number = None
        self.name = name
        self.title = title
        self.rating = rating
        self.rating_type = rating_type
        self.country = country
        self.licence_id = licence_id
        self.birth_date = birth_date
        self.score = score
        self.tie_breaks = list(tie_breaks)
    
    def __repr__(self):
        return f"{self.title if self.title else ' '} {self.name}\t#{self.pairing_number}\t{self.rating}" \
               f"{self.country}, {self.licence_id}, {self.birth_date}" \
               f"\t{self.rating_type}, {self.score} pts\t{self.tie_breaks}"


class DutchPlayer(Player):
    def __init__(self, name: str, rating: int, rating_type, country, licence_id, birth_date, tie_breaks: Iterable,
                 title: Title = Title.NoTitle, score=0, float_status=None, opponents=None,
                 colour_history: List[int] = None):
        super().__init__(name, rating, rating_type, country, licence_id, birth_date, tie_breaks, title, score)
        
        self.float_status = float_status
        self.opponents = list(opponents) if opponents is not None else list()
        self.colour_history = list(colour_history) if colour_history is not None else list()
    
    def __repr__(self):
        return super().__repr__() + f'\t{self.score} pts\t{self.float_status}\t{self.opponents}\t{self.colour_history}'
    
    @property
    def coulour_preference(self):
        return ColourPreference(sum(self.colour_history))
