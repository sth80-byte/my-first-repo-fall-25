import random

#valid options
valid_choices=["rock", "paper", "scissors"]

#input validation loop
while True:
    user_choice=input("Please choose rock, paper, or scissors: ").strip().lower()
    if user_choice in valid_choices:
        break
    else:
        print("Oops! Invalid choice. Please try again with rock, paper, or scissors.")
        print("_______________________")

print(f"{PLAYER_NAME} chose {user_choice}.")
print("_____________________")

#computer chooses randomly
computer_choice=random.choice(valid_choices)
print(f"The computer chose {computer_choice}.")
print("_____________________")

#determine winner
if user_choice==computer_choice:
    print("It's a tie!")
elif user_choice=="rock" and computer_choice=="scissors":
    print("You win! Thanks for playing")
elif user_choice=="paper" and computer_choice=="rock":
    print("You win! Thanks for playing")
elif user_choice=="scissors" and computer_choice=="paper":
    print("You win! Thanks for playing")
else:
    print("You lose! Better luck next time!")
print("___________________")
print("Goodbye and thanks for playing!")