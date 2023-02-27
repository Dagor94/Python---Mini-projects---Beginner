# this game is rock, paper, scissors - The computer will keep track on how many times the user wins the game and how many times the pc wins.

import random

userWins = 0
computerWins = 0
draws = 0

options = ["rock", "paper", "scissors"]

while True:
    userInput = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if userInput == "q":
        print("Thanks for playing")
        break
    
    if userInput not in options:
        print("Wrong input, please follow the instructions.")
        continue

    randomNumber = random.randint(0, 2)
    #* Rock: 0, Paper: 1, Scissors: 2
    computerPick = options[randomNumber]
    print("Computer picked", computerPick + "." )

    #! If the player wins
    if  (userInput == "rock" and computerPick == "scissors") or (userInput == "scissors" and computerPick == "paper") or (userInput == "paper" and computerPick == "rock"):
        print("You won!")
        userWins += 1

    #! If the Computer wins
    elif (computerPick == "rock" and userInput == "scissors") or (computerPick == "scissors" and userInput == "paper") or (computerPick == "paper" and userInput == "rock"):
        print("You won!")
        computerWins += 1
    
    #! If nobody wins    
    else:
        print("its a draw!")
        draws += 1


print("You won", userWins, "times")
print("The computer won", computerWins, "times")
print("It ended in a Draw", draws, "times")
print("Goodbye")





