class Game():

    # need a method to track players
    # need a method to track current player

    players = ['Player', 'Dealer']


    cards  = {
    'ace':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
    'ten':10,
    'jack':10,
    'queen':10,
    'king':10
    }

    suits = [
    'clubs',
    'diamonds',
    'hearts',
    'spades'
    ]

    def __init__(self):
        self.player_cards = []
        self.dealer_cards = []
        self.deck = self.generate_deck()
        self.deal_cards()
        self.display_table()

    # Generates a new deck per game
    def generate_deck(self):
        deck = []
        for suit in Game.suits:
            for key,value in Game.cards.items():
                deck.append((key,value,suit))

        self.shuffle_deck(deck)
        return deck

    # Shuffles the deck
    def shuffle_deck(self, deck):
        from random import shuffle
        return shuffle(deck)


    # Deals out two cards to each player
    def deal_cards(self):
        self.player_cards.append(self.deck.pop(0))
        self.dealer_cards.append(self.deck.pop(0))
        self.player_cards.append(self.deck.pop(0))
        self.dealer_cards.append(self.deck.pop(0))


    # Deal a card from the top of the deck
    def deal_card(self):
        return self.deck.pop(0)


    # Display the current table
    def display_table(self):
        dc1 = self.dealer_cards[0]
        dc2 = self.dealer_cards[1]

        pc1 = self.player_cards[0]
        pc2 = self.player_cards[1]
        print(f'''

        |||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                                   DEALER

                                |{dc1[0]} of {dc1[2]}|
                                |{dc2[0]} of {dc2[2]}|




                                    PLAYER
                                      
                                |{pc1[0]} of {pc1[2]}|
                                |{pc2[0]} of {pc2[2]}|


        |||||||||||||||||||||||||||||||||||||||||||||||||||||||||



        ''')




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
