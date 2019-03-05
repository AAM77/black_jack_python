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

    # Checks if a value is an integer
    def type_int(self,val):
        try:
            int(val)
        except:
            print("Invalid entry.")
        else:
            return val

    # Checks if the input is a one or eleven
    def one_or_eleven(self):
        ace_value = input("Do you want to use it as a 1 or 11?")
        if self.type_int(ace_value):
            ace = int(ace_value)
            if (ace == 1) or (ace == 11):
                return ace
            else:
                print("Must be a 1 or 11.")
                self.one_or_eleven()
        else:
            print("Must be a 1 or 11.")
            self.one_or_eleven()
