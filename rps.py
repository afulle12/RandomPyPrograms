import random, string

tc = 0
bc = 0
pc = 0
percentP = ""
percent = ""
v = True

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    if user_action == "r":
        user_action = "rock"
    elif user_action == "p":
        user_action = "paper"
    elif user_action == "s":
        user_action = "scissors"
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        tc += 1
    elif user_action == "rock" or user_action == "r":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            v = True
            pc += 1
            tc += 1
        else:
            print("Paper covers rock! You lose.")
            v = True
            bc += 1
            tc += 1
    elif user_action == "paper" or user_action == "p":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            v = True
            pc += 1
            tc += 1
        else:
            print("Scissors cuts paper! You lose.")
            v = True
            bc += 1
            tc += 1
    elif user_action == "scissors" or user_action == "s":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            v = True
            pc += 1
            tc += 1
        else:
            print("Rock smashes scissors! You lose.")
            v = True
            bc += 1
            tc += 1
    else:
        v = False
        print("Invalid input! You must pick Rock, Paper, or Scissors (or R, P, S)")
    
    if v == True:
        if tc == 0 and bc == 0:
            percent = "0"
        else:
            intb = (bc / tc)  * 100
            percent = str(intb)[:5]
            intp = (pc / tc)  * 100
            percentP = str(intp)[:5]
        print("\nPlayers win " + percentP + "% of the time.")
        play_again = input("Bots win " + percent + "% of the time\nPlay again? (y/n): ")
    else:
        #print(str(v) + "\n")
        play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y" and play_again.lower != "yes":
        break
