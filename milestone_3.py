import random


class Hangman:
    def __init__(self, word_list, num_lives):

        self.num_lives = num_lives
        self.word_list = word_list

        self.word = random.choice(word_list)
        self.right_guess = list(len(self.word) * ",")
        self.num_letters = len(set(self.word) - set(self.right_guess))
        self.list_of_guesses = []
        
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in word")

            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.right_guess[i] = guess
            self.num_letters -= 1
            
        else:
            self.num_lives -=1
            print(f'Sorry {guess} is not in the word')
            print(f'You have {self.num_lives} lives left')

        self.list_of_guesses.extend(guess)
        
    def ask_for_input(self):
        while True:
            guess = input("Enter a letter:")
            if len(guess) != 1 and guess.isalpha() == False:
                print("Invalid letter. Please enter a single alphabetic character")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                break
            

def play_game():
    game = Hangman(word_list=["apple", "guava", "pear", "berry", "grape"], num_lives=10)
    while True:
        if game.num_lives == 0:
            print("You Lost! {game.word_guessed} is the correct word")
            break
        elif game.num_lives > 0 and game.num_letters <= 0:
            print("Congratulations! You won the game")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
            
        
play_game()    

