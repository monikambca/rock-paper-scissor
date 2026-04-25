import random
import time

class RockPaperScissorsGame:
    def __init__(self):
        # Initialize game state variables
        self.user_score = 0
        self.computer_score = 0
        self.rounds = 0
        self.difficulty = None
        
        # Valid choices in the game
        self.choices = ['rock', 'paper', 'scissors']
    
    def display_title(self):
        """Display game title with formatting"""
        print("\n" + "="*60)
        print("🎮 WELCOME TO ROCK PAPER SCISSORS 🎮".center(60))
        print("="*60 + "\n")
    
    def select_difficulty(self):
        """Prompt user to select difficulty level"""
        print("📊 SELECT DIFFICULTY LEVEL:")
        print("-" * 60)
        print("1. Easy   - Computer plays randomly")
        print("2. Medium - 50% random, 50% counter strategy")
        print("3. Hard   - Computer always counters your moves")
        print("-" * 60)
        
        # Loop until valid input is received
        while True:
            choice = input("Enter difficulty (1/2/3): ").strip()
            if choice in ['1', '2', '3']:
                difficulty_map = {'1': 'easy', '2': 'medium', '3': 'hard'}
                self.difficulty = difficulty_map[choice]
                print(f"\n✅ Difficulty set to: {self.difficulty.upper()}\n")
                return
            
            print("❌ Invalid choice. Please enter 1, 2, or 3.")
    
    def get_user_choice(self):
        """Get and validate user's move"""
        while True:
            user_input = input("🎯 Your choice (rock/paper/scissors) or 'quit': ").lower().strip()
            
            # Allow exit
            if user_input == 'quit':
                return 'quit'
            
            # Validate input
            if user_input in self.choices:
                return user_input
            
            print("❌ Invalid input! Please enter rock, paper, or scissors.")
    
    def get_computer_choice(self, user_choice=None):
        """Generate computer's move based on difficulty"""
        
        # EASY: Completely random
        if self.difficulty == 'easy':
            return random.choice(self.choices)
        
        # MEDIUM: Mix of random and counter strategy
        elif self.difficulty == 'medium':
            if random.random() < 0.5:
                return random.choice(self.choices)
            else:
                return self.get_counter_move(user_choice)
        
        # HARD: Always counter player's move
        elif self.difficulty == 'hard':
            return self.get_counter_move(user_choice)
    
    def get_counter_move(self, user_choice):
        """Return move that defeats the user's choice"""
        counter = {
            'rock': 'paper',
            'paper': 'scissors',
            'scissors': 'rock'
        }
        return counter[user_choice]
    
    def determine_winner(self, user_choice, computer_choice):
        """Determine round outcome"""
        
        # Tie condition
        if user_choice == computer_choice:
            return "tie"
        
        # Winning rules
        winning_moves = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
        }
        
        # Check if user wins
        if winning_moves[user_choice] == computer_choice:
            return "user"
        else:
            return "computer"
    
    def display_round_result(self, user_choice, computer_choice, result):
        """Display round results and update scores"""
        
        print("\n" + "-" * 60)
        print(f"🎯 You chose:      {user_choice.upper()}")
        print(f"💻 Computer chose: {computer_choice.upper()}")
        print("-" * 60)
        
        # Update scores based on result
        if result == "tie":
            print("🤝 IT'S A TIE!")
        elif result == "user":
            print("🎉 YOU WIN THIS ROUND!")
            self.user_score += 1
        else:
            print("😢 COMPUTER WINS THIS ROUND!")
            self.computer_score += 1
        
        self.display_scores()
    
    def display_scores(self):
        """Display current scoreboard"""
        print(f"\n📊 SCORE: You {self.user_score} - {self.computer_score} Computer\n")
    
    def play_round(self):
        """Execute a single round of gameplay"""
        self.rounds += 1
        
        print(f"\n{'='*60}")
        print(f"ROUND {self.rounds}".center(60))
        print(f"{'='*60}\n")
        
        # Get user input
        user_choice = self.get_user_choice()
        
        # Exit condition
        if user_choice == 'quit':
            return False
        
        # Generate computer move
        computer_choice = self.get_computer_choice(user_choice)
        
        # Determine result
        result = self.determine_winner(user_choice, computer_choice)
        
        # Display outcome
        self.display_round_result(user_choice, computer_choice, result)
        
        return True
    
    def display_final_results(self):
        """Display final summary after game ends"""
        
        print("\n" + "="*60)
        print("🏆 FINAL RESULTS 🏆".center(60))
        print("="*60)
        
        print(f"Total Rounds Played: {self.rounds}")
        print(f"Your Score:         {self.user_score}")
        print(f"Computer Score:     {self.computer_score}")
        print(f"Difficulty Level:   {self.difficulty.upper()}")
        print("-" * 60)
        
        # Determine overall winner
        if self.user_score > self.computer_score:
            print("🥇 CONGRATULATIONS! YOU ARE THE CHAMPION! 🥇".center(60))
        elif self.computer_score > self.user_score:
            print("🤖 COMPUTER IS THE CHAMPION! 🤖".center(60))
        else:
            print("🤝 IT'S AN OVERALL TIE! 🤝".center(60))
        
        print("="*60 + "\n")
    
    def play_game(self):
        """Main game loop controller"""
        
        self.display_title()
        self.select_difficulty()
        
        # Game loop
        while True:
            if not self.play_round():
                break
            
            # Ask if player wants another round
            play_again = input("Play another round? (yes/no): ").lower().strip()
            if play_again != 'yes':
                break
        
        # Show final results
        self.display_final_results()


# Entry point
if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.play_game()