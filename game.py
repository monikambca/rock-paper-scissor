import random
import time

class RockPaperScissorsGame:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0
        self.rounds = 0
        self.difficulty = None
        self.choices = ['rock', 'paper', 'scissors']
    
    def display_title(self):
        """Display game title with formatting"""
        print("\n" + "="*60)
        print("🎮 WELCOME TO ROCK PAPER SCISSORS 🎮".center(60))
        print("="*60 + "\n")
    
    def select_difficulty(self):
        """Let user select difficulty level"""
        print("📊 SELECT DIFFICULTY LEVEL:")
        print("-" * 60)
        print("1. Easy   - Computer plays randomly")
        print("2. Medium - Computer uses smart strategy (50% random, 50% counter)")
        print("3. Hard   - Computer always counters your moves")
        print("-" * 60)
        
        while True:
            choice = input("Enter difficulty (1/2/3): ").strip()
            if choice in ['1', '2', '3']:
                difficulty_map = {'1': 'easy', '2': 'medium', '3': 'hard'}
                self.difficulty = difficulty_map[choice]
                print(f"\n✅ Difficulty set to: {self.difficulty.upper()}\n")
                return
            print("❌ Invalid choice. Please enter 1, 2, or 3.")
    
    def get_user_choice(self):
        """Get validated user input"""
        while True:
            user_input = input("🎯 Your choice (rock/paper/scissors) or 'quit' to exit: ").lower().strip()
            if user_input == 'quit':
                return 'quit'
            if user_input in self.choices:
                return user_input
            print("❌ Invalid input! Please enter rock, paper, or scissors.")
    
    def get_computer_choice(self, user_choice=None):
        """Get computer choice based on difficulty level"""
        if self.difficulty == 'easy':
            return random.choice(self.choices)
        
        elif self.difficulty == 'medium':
            # 50% random, 50% counter strategy
            if random.random() < 0.5:
                return random.choice(self.choices)
            else:
                return self.get_counter_move(user_choice)
        
        elif self.difficulty == 'hard':
            # Always counter the user's move
            return self.get_counter_move(user_choice)
    
    def get_counter_move(self, user_choice):
        """Return the move that beats the user's choice"""
        counter = {
            'rock': 'paper',
            'paper': 'scissors',
            'scissors': 'rock'
        }
        return counter[user_choice]
    
    def determine_winner(self, user_choice, computer_choice):
        """Determine the winner of a round"""
        if user_choice == computer_choice:
            return "tie"
        
        winning_moves = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
        }
        
        if winning_moves[user_choice] == computer_choice:
            return "user"
        else:
            return "computer"
    
    def display_round_result(self, user_choice, computer_choice, result):
        """Display formatted round result"""
        print("\n" + "-" * 60)
        print(f"🎯 You chose:      {user_choice.upper()}")
        print(f"💻 Computer chose: {computer_choice.upper()}")
        print("-" * 60)
        
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
        """Display current scores"""
        print(f"\n📊 SCORE: You {self.user_score} - {self.computer_score} Computer\n")
    
    def play_round(self):
        """Play a single round"""
        self.rounds += 1
        print(f"\n{'='*60}")
        print(f"ROUND {self.rounds}".center(60))
        print(f"{'='*60}\n")
        
        user_choice = self.get_user_choice()
        if user_choice == 'quit':
            return False
        
        computer_choice = self.get_computer_choice(user_choice)
        result = self.determine_winner(user_choice, computer_choice)
        self.display_round_result(user_choice, computer_choice, result)
        
        return True
    
    def display_final_results(self):
        """Display final game results"""
        print("\n" + "="*60)
        print("🏆 FINAL RESULTS 🏆".center(60))
        print("="*60)
        print(f"Total Rounds Played: {self.rounds}")
        print(f"Your Score:         {self.user_score}")
        print(f"Computer Score:     {self.computer_score}")
        print(f"Difficulty Level:   {self.difficulty.upper()}")
        print("-" * 60)
        
        if self.user_score > self.computer_score:
            print("🥇 CONGRATULATIONS! YOU ARE THE CHAMPION! 🥇".center(60))
        elif self.computer_score > self.user_score:
            print("🤖 COMPUTER IS THE CHAMPION! 🤖".center(60))
        else:
            print("🤝 IT'S AN OVERALL TIE! 🤝".center(60))
        
        print("="*60 + "\n")
    
    def play_game(self):
        """Main game loop"""
        self.display_title()
        self.select_difficulty()
        
        while True:
            if not self.play_round():
                break
            
            play_again = input("Play another round? (yes/no): ").lower().strip()
            if play_again != 'yes':
                break
        
        self.display_final_results()

# Run the game
if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.play_game()