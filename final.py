import random

# Creating the player
class Player:
    def playerInfo(self, name):
        self.name = name  # Storing the player's information
        self.score = 0  # Creating the scoring system for the player

    def roll_dice(self):
        """Rolls three dice and returns the results within a list"""
        return [random.randint(1, 6) for _ in range(3)]

# Define the main game function
def play_game(rounds):
    """Simulating the dice game over what ever amount of rounds you want."""
    # Creating the 2 players utilizing the class from before
    player1 = Player()
    player1.playerInfo("Player 1")
    player2 = Player()
    player2.playerInfo("Player 2")

    # For loop that plays out the specified number of rounds
    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")

        # Player 1's turn
        print(f"{player1.name}'s turn:")
        player1.score += take_turn(player1)
        print(f"{player1.name}'s total score: {player1.score}\n")

        # Player 2's turn
        print(f"{player2.name}'s turn:")
        player2.score += take_turn(player2)
        print(f"{player2.name}'s total score: {player2.score}\n")

    # Figuring out the winner
    print("\n--- Game Over ---")
    if player1.score > player2.score:
        print(f"{player1.name} wins with {player1.score} points!")
    elif player2.score > player1.score:
        print(f"{player2.name} wins with {player2.score} points!")
    else:
        print("It's a tie!")

# Define the function for taking a single turn
def take_turn(player):
    """Simulate a single turn for the given player."""
    dice = player.roll_dice()
    print(f"Initial roll: {dice}")

    while True:
        # Checks if player "tupled out"
        if dice[0] == dice[1] == dice[2]:
            print("Tupled out! You score 0 points this turn.")
            return 0

        # Checks for fixed dice
        fixed_value = None
        if dice[0] == dice[1] or dice[0] == dice[2]:
            fixed_value = dice[0]
        elif dice[1] == dice[2]:
            fixed_value = dice[1]

        # Code that allows rerolling for non fixed dice
        if fixed_value is not None:
            print(f"Two dice are fixed with value {fixed_value}.")
            # Determine the index of the non-fixed die
            non_fixed_index = dice.index(min(dice, key=lambda x: x != fixed_value))
            roll_again = input("Do you want to re-roll the non-fixed die? (yes/no): ").strip().lower()

            if roll_again == "yes":
                dice[non_fixed_index] = random.randint(1, 6)
                print(f"New roll: {dice}")
            else:
                break
        else:
            # If no dice are fixed, allow re-rolling all dice
            roll_again = input("Do you want to re-roll all dice? (yes/no): ").strip().lower()

            if roll_again == "yes":
                dice = player.roll_dice()
                print(f"New roll: {dice}")
            else:
                break

    # Calculate the score for the given turn
    turn_score = sum(dice)
    print(f"You scored {turn_score} points this turn.")
    return turn_score

# Running the game
print("Welcome to Tuple Out!")
rounds = int(input("Enter the number of rounds to play: "))
play_game(rounds)