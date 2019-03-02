class Player():

    def __init__(self, bank_roll):
        self.bank_roll = bank_roll


    def place_bet(self):
        try:
            amount = int(input("How much do you want to bet? "))
            if (type(amount) == int) and (amount >= 0):
                return amount
        except:
            print("Invalid entry. Must be a number.")
            self.place_bet()


    def hit_or_stay(self):
        choice = input("Do you want to hit or stay?").lower()
        if choice == 'hit':
            return True
        elif choice == 'stay':
            return False
        else:
            print("Invalid entry.")
            self.hit_or_stay()
