import random

#valid options
valid_choices=["rock", "paper", "scissors"]

def generate_random_choice():
    return random.choice(valid_choices)

def determine_winner(u, c):
    if u == c:
        return "It's a tie!"
    elif u =="rock" and c =="scissors":
        return "You win! Thanks for playing"
    elif u =="paper" and c =="rock":
        return "You win! Thanks for playing"
    elif u =="scissors" and c =="paper":
        return "You win! Thanks for playing"
    else:
        return "You lose! Better luck next time!"

if __name__ == "__main__":
    #  ONLY RUN THE CODE BELOW
    # IF WE ARE RUNNING THIS SCRIPT FROM THE COMMAND LINE
    # BUT NOT IF WE ARE TRYING TO JUST IMPORT SOME STUFF FROM THIS FILE

    #input validation loop
    

    
    while True:
        user_choice=input("Please choose rock, paper, or scissors: ").strip().lower()
        if user_choice in valid_choices:
            break
        else:
            print("Oops! Invalid choice. Please try again with rock, paper, or scissors.")
            print("_______________________")

    print(f"You chose {user_choice}.")
    print("_____________________")

    #computer chooses randomly
    #computer_choice=random.choice(valid_choices)
    computer_choice = generate_random_choice()
    print(f"The computer chose {computer_choice}.")
    print("_____________________")

    #Determine the winner
    # quick alias
    u = user_choice
    c = computer_choice
 
    result = determine_winner(user_choice, computer_choice)
    print(result)
    



