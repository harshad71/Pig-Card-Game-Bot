from .utils import Deck, Card, CardSet
from dataclasses import dataclass


@dataclass
class GameConfig:
    min_users: int
    max_users: int
    

class PigConfig(GameConfig):
    min_users = 2
    max_users = 4


class Pig:
    
    def __init__(self, users_amount: int, main_deck_hash: str) -> None:
        self.users_amount = users_amount
        self.main_deck_hash = main_deck_hash

    @classmethod
    async def create(cls, users_amount: int) -> 'Pig':
        ''' '''
        data = await Deck.get_new_shuffled_deck()
        hash = data['deck_id']
        return cls(users_amount, hash)

    async def card_matching(current_card: Card, new_card: Card) -> bool:
        if (current_card.rank == new_card.rank) or (current_card.suit == new_card.suit):
            return True
        return False
    
    async def flip_card():
        ...

    async def pass_deck(user_id: int):
        ...