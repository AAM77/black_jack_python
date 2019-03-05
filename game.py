class Game():

    # need a method to track players
    # need a method to track current player

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
        self.game_deck = generate_deck
        self.deal_cards()

    # Generates a new deck per game
    def generate_deck():
        deck = []
        for suit in suits:
            for card in cards:
                deck.append((suit,card))
        return deck


    # Deals out two cards to each player
    # def deal_cards(self):
        # player_cards = []
        # dealer_cards = []
        # remove a card from the top of the deck and deal it to player 1
        # (append it to player_cards)
        # remove a card from the top of the deck and deal it to player 2
        # (append it to dealer_cards)
        # remove a card from the top of the deck and deal it to player 1
        # (append it to player_cards)
        # remove a card from the top of the deck and deal it to player 2
        # (append it to dealer_cards)
        # self.player_cards = player_cards
        # self.dealer_cards = dealer_cards


    # Deal a card from the top of the deck
    def deal_card(self):
        return self.deck.pop(0)


    # Display the current table
    # def display_table(self):
        # print('''
        # ||||||||||||||||||||||||||||||
        # ||           DEALER         ||
        # ||         __     __        ||
        # ||        |  |   |  |       ||
        # ||        |__|   |__|       ||
        # ||                          ||
        # ||                          ||
        # ||                          ||
        # ||           PLAYER         ||
        # ||         __     __        ||
        # ||        |  |   |  |       ||
        # ||        |__|   |__|       ||
        # ||                          ||
        # ||||||||||||||||||||||||||||||
        #
        # ''')

    # Shuffles the deck
    def shuffle_deck(self):
        from random import shuffle
        return shuffle(self.deck)


    # Checks the sum of the current_player's cards
    # def check_sum(self):
        # if the sum is greater than 21:
            # the current player loses
        # else if the sum is 21:
            # go to the next turn
        # else if the sum is less than 21:
            # ask the player if s/he would like to hit or stay
