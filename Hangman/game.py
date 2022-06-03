from player import Player
import random
from art import stages,logo
from word import word_list

class Game:
    def __init__(self):
        self.player = Player()
        self.display = []
        self.chosen_word = random.choice(word_list)
    

    def display_welcome(self):
        print(logo)
    
    def run_game(self):
        self.display_welcome()
        self.play_game()

    def play_game(self):
        self.word_length = self.spaces_for_letters()
        while self.player.lives > 0:
            self.check_letter()
            print(f' '.join(self.display))
            self.stages()
            if "_" not in self.display:
                self.player.lives == 0
                print("You win! ")
                return
            elif self.player.lives == 0:
                print(f"The chosen word was: {self.chosen_word}")
                print("You lose")

    def check_letter(self):
        guess = self.player.pick_a_letter()
        for index in range(self.word_length):
            letter = self.chosen_word[index]
            if letter == guess:
                self.display[index] = letter
            
        if guess not in self.chosen_word:
            print(f"{guess} is not in the word. You lose a life")
            self.player.lives -= 1

    def spaces_for_letters(self):
        word_length = len(self.chosen_word)
        for _ in range(word_length):
            self.display += "_"
        print(f' '.join(self.display))
        return word_length

    def stages(self):
        print(stages[self.player.lives])