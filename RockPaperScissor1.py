#Write a Python program that simulates the "Rock, Paper, Scissors" game.
#The game should ask the user to enter an option (either "Rock", "Paper", or "Scissors").
#The player should play against the computer, which will select a random option.
#The computer's selection will be compared against the player's selection to determine who wins.
#A descriptive message should be displayed indicating if the player won, lost, or if the game 
#ended in a tie.
import random

choices=['paper','rock','scissors'] 

computer_input=random.choice(choices)

print("====== Welcome to the game ======")
user_input=input("Please enter \"Rock\", \"Paper\", or \"Scissors\" below: ").lower()

print(f"User input: {user_input}")
print(f"Computer input: {computer_input}\n")


if (user_input == "paper"):
    if(computer_input=="rock"):
        print("Paper beats Rock\n")
        print("You win! Computer chose \"Rock\"")
    elif(computer_input=="scissors"):
        print("Scissors beat Paper.\n")
        print("You lose! Computer chose \"Scissors\"") 

    elif(computer_input=="paper"):
        print("It's a tie! Try again.") 


elif (user_input == "rock"):
    if(computer_input=="scissors"):
        print("Rock beats Scissors")
        print("You win! Computer chose \"Scissors\"")
    
    elif(computer_input=="paper"):
        print("Paper beats Rock.")
        print("You lose! Computer chose \"Paper\"") 
    elif(computer_input=="rock"):
        print("It's a tie! Try again.")


elif (user_input == "scissors"):
    if(computer_input=="paper"):
        print("Scissors beat Paper.")
        print("You win! Computer chose \"Paper\"")

    elif(computer_input=="rock"):
        print("Rock beats Scissors.")
        print("You lose! Computer chose \"Rock\"")
    elif(computer_input=="scissors"):
        print("It's a tie! Try again.")


else:
    print("Invalid user input.")



