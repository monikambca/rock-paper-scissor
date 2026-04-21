import random

# Function to get the user's choice
def get_user_choice():
    user_input = input("Enter Rock, Paper, or Scissors: ").lower()
    while user_input not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please try again.")
        user_input = input("Enter Rock, Paper, or Scissors: ").lower()
    return user_input

# Function to get the computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    return computer_choice

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

# Main game loop
if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)