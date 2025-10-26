import random

our_selection = input ("Choose Your Fighter! rock, paper, scissors")
choices = ["rock", "paper","scissors"]

print("You Chose",{our_selection})


computer = random.choice(choices)
print("The comptuer chose", {computer})

if our_selection == computer:
    print("You both chose",{our_selection},"its a tie!")
elif our_selection == "rock":
    if computer == "scissors":
        print("Rock beats scissors, You Won!")
    else:
        print("Paper beats rock, You lose!")
elif our_selection == "paper":
    if computer == "rock":
        print("Paper beats rock, You Won!")
    else:
        print("Scissors cut paper, You lose!")    
elif our_selection == "scissors":
    if computer == "paper":
        print("Scissors cut paper, You Won!")
    else:
        print("Rock beats scissors, You lose!") 
elif our_selection != choices:
    print("Please choose a valid fighter !")   





