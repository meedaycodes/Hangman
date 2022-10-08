# hangman
##Milestone 1
- This is a basic python program that performs two functions
- The first function  returns a random word from a list of fruits provided using the random.choice method
```
word_list = ["Apple", "Pear", "Orange", "Grapes", "Guava"]
    word = random.choice(word_list)
    print(word)
```
- The second function gets an input from the user and saves the input in a variable called "guess"
- checks if the length ia equal to 1 and if the user is an alphabet
- And prints out an output based on the values the user inputs
```
guess = input("Enter a single letter here:")
if len(guess) == 1 and guess.isalpha():
    print("Good guess")
else:
    print("Ooops, That's not a valid input")
```
##Milestone 2
- This second milestone of the game adds 2 functionalities to it
- The first fuction converts the user's guess to lowercase with thw lower() and checks if the guess is in the word variable from milestone 1
```
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f'Good guess. {guess} is in the word')
    else:
        print(f'Sorry, {guess} is not in the word.Try again')
 ```
- The second function checks that the user has provided a single alphabet character and breaks the while loop that iteratively asks for a valid input
- the first function is then called within this function but outside the while loop
```
def ask_for_input():
    while True:
        guess = input("Enter an alphabet: ")

        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please enter a single alphabetic character")
            
    check_guess(guess)
   ```
   ##Milestone 3
  - In this milestone the Hangman class was created and was initialised with two parameters(word_list, num_lives) within the init constructor
  - Four other class variables self(word, word_guessed, num_lives, lIst_of_guesses) were defined within the constructor method
  ```
  class Hangman:
    def __init__(self, word_list, num_lives=5):
        
        self.num_lives = num_lives
        self.word_list = word_list

        self.word = random.choice(word_list)
        self.word_guessed = [str(a) for a in self.list_of_guesses]
        self.num_letters = len(set(self.word) - set(self.word_guessed))
        self.list_of_guesses = []
  ```
  - The second method check_guess allows for the verification of the letter provided by the user,
  - First it checks if the guess is in the word variable, if this condition is met, it appends the letter into the list of word_guessed indexing it at a particular position
 - if this conditions are not met the else block of the code runs
  ```
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
 ```
 - The last method ask_for_input() gets the input from the user and checks for two conditions within the while loop
 1. if the length of the guess is 1
 2. if the guess is an alphabet

 ```
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
```
