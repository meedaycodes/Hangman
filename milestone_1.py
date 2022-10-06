import random


word_list = ["Apple", "Pear", "Orange", "Grapes", "Guava"]
word = random.choice(word_list)
print(word)

guess = input("Enter a single letter here:")

if len(guess) == 1 and guess.isalpha():
    print("Good guess")
else:
    print("Ooops, That's not a valid input")

