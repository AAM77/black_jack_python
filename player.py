class Player():

    def __init__(self, bank_roll):
        self.bank_roll = bank_roll


    # Display's the user's current bank_roll
    def display_bank_roll(self):
        print(self.bank_roll)

    # Give the user an opportunity to play a bet
    def place_bet(self):
        try:
            amount = int(input("How much do you want to bet? "))
            if (type(amount) == int) and (amount >= 0):
                return amount
        except:
            print("Invalid entry. Must be a number.")
            self.place_bet()

    # Allows the user to choose to draw a new card (hit)
    # or keep the current hand (stay)
    def hit_or_stay(self):
        choice = input("Do you want to hit or stay?").lower()
        if choice == 'hit':
            return True
        elif choice == 'stay':
            return False
        else:
            print("Invalid entry.")
            self.hit_or_stay()

    # Allows the user to choose if s/he wants
    # Ace to be a 1 or 11
    ## !!!!!!!!!!!!!!! NEED TO FIX !!!!!!!!!!!!!!!!
    def one_or_eleven(self):
        try:
            ace_value = int(input("Do you want ace to be a 1 or 11? "))
            if (ace_value == 1) or (ace_value == 11):
                return ace_value
        except:
            print("Invalid entry. Must be a 1 or 11.")
            self.one_or_eleven()
