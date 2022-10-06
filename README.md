# hangman
##Milestone-1
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
    
