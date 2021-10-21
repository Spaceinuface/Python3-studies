from random import randint
import sys
 
guess_this_number = randint(1,10)
guess = 0
guesses = 0
clue = ""
first_round = True
 
 
while guess != guess_this_number:
 
    if first_round == True:
        guess = int(input("Enter an integer number: "))
        first_round = False;
    else:
       print("- - - - - - - - - - - - - - - -")
       print(guess, clue)
       guess = int(input("Guess again: "))
 
    if (guess < guess_this_number):
        clue = "is too low!"
    else:
        clue = "is too high!"
    guesses += 1
 
print("- - - - - - - - - - - - - - - - - - - - - - - -")
print(guess_this_number, "is correct and you made it in ", guesses, " guesses!")
print("- - - - - - - - - - - - - - - - - - - - - - - -")