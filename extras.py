"""ROCK, PAPER, SCISSORS GAME"""

import random

computer_guess = ["rock", "paper", "scissors"]
user_guess = input("Enter your choice: rock, paper, scissors: ").lower()
#computer_guess = random.choice(computer_guess)

# Ensure user enters a valid choice
if user_guess not in computer_guess:
    print("Invalid choice. Please enter rock, paper, or scissors.")
else:
    # Computer makes a random choice
    computer_choice = random.choice(computer_guess)
    
    # Display the choices
    print(f"You chose: {user_guess}")
    print(f"Computer chose: {computer_choice}")
    
    # Determine the winner
    if user_guess == computer_choice:
        print("It's a tie!")
    elif (user_guess == "rock" and computer_choice == "scissors"):
        print("You win!")
    elif (user_guess == "scissors" and computer_choice == "paper"):
        print("You win!")
    elif (user_guess == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")

