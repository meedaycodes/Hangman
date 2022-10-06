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
