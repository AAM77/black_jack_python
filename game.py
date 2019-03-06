class Game():

    # need a method to track players
    # need a method to track current player

    players = ['Player', 'Dealer']


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

    def __init__(self):
        self.player_cards = []
        self.dealer_cards = []
        self.deck = generate_deck
        self.shuffle_deck()
        self.deal_cards()

    # Generates a new deck per game
    def generate_deck():
        deck = []
        for suit in suits:
            for card in cards:
                deck.append((suit,card))
        return deck


    # Deals out two cards to each player
    def deal_cards(self):
        self.player_cards.append(self.deck.pop(0))
        self.dealer_cards.append(self.deck.pop(0))
        self.player_cards.append(self.deck.pop(0))
        self.dealer_cards.append(self.deck.pop(0))


    # Deal a card from the top of the deck
    def deal_card(self):
        return self.deck.pop(0)


    Display the current table
    def display_table(self):
        dc1 = self.dealer_cards[0]
        dc2 = self.dealer_cards[1]

        pc1 = self.player_cards[0]
        pc2 = self.player_cards[1]
        print(f'''

        ||||||||||||||||||||||||||||||
        ||           DEALER         ||
        ||                          ||
        ||     |{dc1}|   |{dc2}|    ||
        ||                          ||
        ||                          ||
        ||                          ||
        ||                          ||
        ||           PLAYER         ||
        ||                          ||
        ||     |{pc1}|   |{pc2}|    ||
        ||                          ||
        ||                          ||
        ||||||||||||||||||||||||||||||

        ''')

    # Shuffles the deck
    def shuffle_deck(self):
        from random import shuffle
        return shuffle(self.deck)


    # Checks the sum of the current_player's cards
    def check_sum(self):
        if sum(self.player_cards) > 21:
            print("Player loses")
        elif sum(self.player_cards) == 21:
            # go to the next turn
            pass
        elif sum(self.player_cards) < 21:
            # ask the player if s/he would like to hit or stay
            print("Do you want to hit or stay?")
            pass
