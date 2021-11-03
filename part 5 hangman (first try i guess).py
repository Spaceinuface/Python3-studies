# This is not what I invisioned as my hangman game tried to do it the correct way but couldnt for the life of me figure out how.
# I wanted the progress to be filled presented each loop with dashes for jet not guessed letters and the letters that where correct 
# filled out but after trying to figure that out for 2 hours I did this pice if crap instead.

import random

words = ["bad", "bil", "båt"]
word = random.choice(words)

hp = 5
guesses = ""
length = len(word)
correct = 0

print("Guess a character in the secret word")


while hp > 0:
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("")
    if correct == length:
        print(f"you win! The word was {word}!")

    guess = input("Guess a character ")
    guesses += guess
    if guess in word:
        print(F"Correct {guess} is in the word")
        correct += 1

    if guess not in word:
        hp -= 1
        print(f"Wrong! You have {hp} hp left")

        if hp == 0:
            print("You lose. :(")
