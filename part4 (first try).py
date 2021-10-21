import sys
import random
import time

user = 0
round = 0
user_wins = 0
comp_wins = 0
play_more = ""
quit_time = 3
sec = 3
terminate = False

while terminate == False:
    
    #THE ACTUAL ROUND OF PLAYZ
    rounds = int(input("How many rounds do you wanna play? "))
    while round < rounds:
        round += 1
        comp = random.randint(1,3)
        print("1 = Rock - 2 = Siccor - 3 = Papper - 4 to quit playing!")
        user = int(input("What is your pick? "))

        # CALCULATE WINNER!
        # LAZY ME NO PROPER ANNOUNCENT ON COMPUTER WINS, I WILL REDO THIS THE CORRECT WAY WHEN AVAILABLE_TIME > 0 :(
        if user == comp:
            print("DRAAAAAW!!!")
        elif user == 1 and comp == 2:
            print("YOU WON! Rock beats Siccor")
            user_wins += 1
        elif user == 2 and comp == 3:
            print("YOU WON! Siccor beats papper!")
            user_wins += 1
        elif user == 3 and comp == 1:
            print("YOU WON! Papper beats rock!")
            user_wins += 1
        elif user == 4:
            terminate == True
            print("U gave up early!")
        else:
            print("Computer won this one, better luck next round!")
            comp_wins += 1

    # ANNOUNCE THE WINNER
    if user_wins == comp_wins:
        print(f"It was a draw match {comp_wins} / {user_wins}")
    elif user_wins > comp_wins:
        print(f"You won this match {user_wins} / {comp_wins}")
    else:
        print(f"Computer won this match {comp_wins} / {user_wins}")

    # ASK USER TO PLAY MORE

    play_more = input("Want to play again? y = Yes / n = No . . . : ")
    while play_more not in ["y", "Y", "n", "N"]:
        if play_more == ["y", "Y"]:
            comp_wins = 0
            user_wins = 0
            for x in sec:
                print("Restart in:", sec)
                sec -= 1
                if sec == 0:
                    break
        elif play_more == ["n", "N"]:
            print("Was fun playing with you ;) Cya later!")
            terminate = True
            for x in sec:
                print("Closing in:", sec)
                sec -= 1
                if sec == 0:
                    break
        else:
            play_more = input("Invlaid input! You wanna play again? valid inputs: Y / N: ")