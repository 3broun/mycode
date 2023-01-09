# computer needs to make a choice
# choices need to be evaluated
# print out the result (who won)
import random

def main():
    """body of the game"""
    
    choice= input("Rock, Paper, or Scissors?\n>")
    botchoice= random.choice(["rock", "paper", "scissors"])

    choice= choice.lower() # validates input by forcing input to be lower case

    # uncomment these print functions to debug
    #print(choice)
    #print(botchoice)

    if choice not in ["rock", "paper", "scissors"]:
        print("You entered an invalid choice, you lose(r)!")

    elif choice == "scissors" and botchoice == "paper":
        print("You win!")
    # user picked scissors... did they win or lose?

    ### ADD MORE HERE
    elif choice == "paper" and botchoice == "rock":
        print("You win")

    elif choice == "rock" and botchoice == "scissors":
        print("You win!")
   
    elif choice == "rock" and botchoice == "paper":
        print("You lose!")

    elif choice == "paper" and botchoice == "scissors":
        print("You lose!")

    elif choice == "scissors" and botchoice == "rock":
        print("You lose!")

    else: 
        print("It's a tie")




main()
