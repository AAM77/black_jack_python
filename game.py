class Game():

    cards  = [
    'ace',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'jack',
    'queen',
    'king'
    ]

    suits = [
    'clubs',
    'diamonds',
    'hearts',
    'spades'
    ]

    # Generates a new deck per game
    def generate_deck():
        deck = []
        for suit in suits:
            for card in cards:
                deck.append((suit,card))
        return deck
