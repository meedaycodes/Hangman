import random


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = [str(a) for a in self.list_of_guesses]
        self.num_letters = len(set(self.word) - set(self.word_guessed))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        self.guess = guess.lower()
        if self.guess in self.word:
            print(f"Good guess! {guess} is in word")
            for i, letter in enumerate(self.word):
                if letter == self.guess:
                    self.word_guessed[i] = self.guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry {letter} is not in the word')
            print(f'You have {self.num_lives} left')
        self.list_of_guesses.append(guess)

    def ask_for_input(self):
        while True:
            guess = input("Enter a letter: ")
            if len(guess) != 1 and guess.isalpha() == False:
                print("Invalid letter. Please enter a single alphabetic character")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
