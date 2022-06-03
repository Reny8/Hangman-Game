class Player:
    def __init__(self):
        self.lives = 6

    
    def pick_a_letter(self):
        guess = input("Guess a letter: ").lower()
        return guess 