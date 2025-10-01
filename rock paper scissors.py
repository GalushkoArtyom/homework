import random

a = random.randint(0, 2)
rock = 0
paper = 1
scissors = 2
action = input("make a choice: rock, paper or scissors: ")
if action == "rock":
    player_choice = rock
elif action == "paper":
    player_choice = paper
elif action == "scissors":
    player_choice = scissors
else:
    print("Invalid input! Please choose rock, paper or scissors.")
    exit()
print(f"Computer chose: {a}")
if a == player_choice:
    print('Draw!')
elif (a == rock and player_choice == scissors) or \
     (a == paper and player_choice == rock) or \
     (a == scissors and player_choice == paper):
    print('You lost, computer wins :(')
else:
    print('You won, computer lost!')