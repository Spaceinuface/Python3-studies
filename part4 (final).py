import sys
import random


user_choice = "a"
choices = ["rock", "scissor", "papper"]
game_on = True
ask_if_play = ""

# # # REDEFINES USERS 1KEY COMMAND TO A FULL WORD
def rewrite(user_choice):
    if user_choice == "r":
        return "rock"
    elif user_choice == "s":
        return "scissor"
    elif user_choice == "å":
        return "Space is dumb"
    elif user_choice == "p":
        return "papper"
    else:
        return ""

# # # PLAY WHILE USER FEELS LIKE IT
while game_on == True:
    print("! ! ! ! ! ALTERNATIVES: R = rock, P = papper, S = scissors:")
    user_choice = rewrite(input("? ? ? ? ? ? Rock, papper scissor gooooo! ").lower())

    # # # VALIDATE USER INPUT
    while user_choice == "":
        print("# # # # INVLAID INPUT! # # # # # ")
        user_choice = rewrite(input("? ? ? ? ? ? VALID INPUT: R = rock, P = papper, S = scissor: ").lower())

    # SAVING THIS BECAUSE THE AGONY!!!!!!! 3 HOURS OF BEAING MY FACE AGAINS A BRICK WALL!
    # I WROTE THIS FIRST:
    lul = "choices.pop(random.randint(1,3)-1)"
    # COULDNT FIGURE OUT THE PROBLEM TRIED choices.pop(random.randint(0,2)+1), (1,2)-1), (0,3)-1) and sadly more... much much more!
    # I NEED TO GET BETTER AT FINDING SOLUTIONS FOR PROBLEM LIKE THIS :'( AAAAAAALL THE WRONG GOOGLES GG SPACE :'(
    
    # # # COMPUTER RANDOMS IT'S CHOICE 
    cpu_choice = random.choice(choices)                                    
                                                                                                                     
    # # # CALCULATE WINNER                                                                                          
    if user_choice == cpu_choice:                                                               
        print("! ! ! ! ! !  DRAW! ! ! ! ! ! ! ")                                                                                  
    elif user_choice == "rock" and cpu_choice == "scissor":
        print(f"! ! ! ! ! !  You win! {user_choice} beats {cpu_choice} ! ! ! ! ! ! ! ")
    elif user_choice == "papper" and cpu_choice == "rock":
        print(f"! ! ! ! ! !  You win! {user_choice} beats {cpu_choice} ! ! ! ! ! ! ! ")
    elif user_choice == "Space is dumb": 
        print(f"! ! ! ! ! !  Space loses! {user_choice} becuase {lul} ! ! ! ! ! ! ! ")
    elif user_choice == "scissor" and cpu_choice == "papper":
        print(f"! ! ! ! ! !  You win! {user_choice} beats {cpu_choice} ! ! ! ! ! ! ! ")
    else:
        print(f"! ! ! ! ! !  Computer wins! {cpu_choice} beats {user_choice} ! ! ! ! ! ! ! ")

    
    # # # # ASK IF USER WANTS TO CONTINUE
    ask_if_play = input("? ? ? ? ? ? Play more? Y = Yes / N = No ").lower()
    if ask_if_play == "n":
        game_on = False

    

