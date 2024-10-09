#Write a Python program that simulates the "Rock, Paper, Scissors" game.
#The game should ask the user to enter an option (either "Rock", "Paper", or "Scissors").
#The player should play against the computer, which will select a random option.
#The computer's selection will be compared against the player's selection to determine who wins.
#A descriptive message should be displayed indicating if the player won, lost, or if the game 
#ended in a tie.
import random

choices=('paper','rock','scissors')
computer_input = choices[random.randint(0,2)]

print("====== Welcome to the game ======")
user_input=input("Please enter \"Rock\", \"Paper\", or \"Scissors\" below: ").lower()


if user_input==computer_input:
    print("It's a tie! Try again.") 
elif user_input=="rock":
    if computer_input=="paper":
        print("You lose! Computer chose \"Paper\"") 
    else:
        print("You win! Computer chose \"Scissors\"") 

elif user_input=="paper":
    if computer_input=="scissors":
        print("You lose! Computer chose \"scissors\"") 
    else:
        print("You win! Computer chose \"Rock\"") 

elif user_input=="scissor":
    if computer_input=="rock":
        print("You lose! Computer chose \"Rock\"") 
    else:
        print("You win! Computer chose \"Paper\"") 

else:
    print("Invalid user input.")   