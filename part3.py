import sys
import random

secret_number = int(input("Give me a number 1 - 100 then ill try and guess it: "))
guess = random.randint(1,100)
clue = ""
high_roof = 100
low_roof = 1

print("#############################################")
print("######## SECRET #", secret_number, "#########")
print("##############################################")
print(" ")
while guess != secret_number:

    print("Im guessing: ", guess, "And it's WRONG I just know it!")
    clue = input("Tell me if its too high or low: ")


    while clue not in ["high","low"]:
        print("Your input is invalid!")
        clue = input("Tell me if its too high or low: ")
    if clue == "high":
        high_roof = guess - 1
        guess = random.randint(low_roof,high_roof)
        print("lol")
    else:
        low_roof = guess + 1
        guess = random.randint(low_roof,high_roof)
print(" ")
print(" ")
print(" ")
print("I knew it all along the secret number is: ", guess)
print(" ")
print(" ")
