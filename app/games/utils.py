import aiohttp

from typing import Any


class Deck:
    '''The class to manage API requests to https://deckofcardsapi.com/api
    
       Methods
       -------
       get_new_shuffled_deck()
           returns a new <i>shuffled</i> deck
           endpoint: https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=

       get_deck_cards()
           returns cards from a <i>particular</i> deck
           endpoint: https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=
    '''

    @classmethod
    async def get_new_shuffled_deck(self) -> dict[str, Any]:
        '''The method to get a new shuffled deck.\n
           
            Parameters
            ----------
            No parameters

            Returns
            -------
            API response : dict[str, Any]

            <b>NOTE:</b> the returned deck is already shuffled!
        
            Example response
            -----------------
            <code>{"success": true,   
                   "deck_id": "3p40paa87x90",  
                   "shuffled": true,
                   "remaining": 52}</code>
        '''

        url = 'https://deckofcardsapi.com/api/deck/new/shuffle/'
        params = {'deck_count' : 1}
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                data = await response.text()
        return data
    
    @classmethod
    async def get_deck_cards(self, deck_id: str, count: int = 1) -> dict[str, Any]:
        '''The method to get cards from a particular deck.\n    
        
            Parameters
            ----------
            deck_id : str, required
            unique deck hash;
            count : int, optional
            amount of cards to get (default = 1);
        
            Returns
            -------
            API response : dict[str, Any]
        '''

        url = f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/'
        params = {'count' : count}
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                data = await response.text()
        return data
            

class CardSet:
    def __init__(self, user_id: int, battle_id: int) -> None:
        self.user_id = user_id
        self.battle_id = battle_id
        self.hash = None

    def __iter__(self):
        return self

    def __next__(self):
        ...
    
    async def generate_new():
        ...



class Card:
    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit
