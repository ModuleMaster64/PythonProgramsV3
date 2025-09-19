import random

def roll_dice(sides=6):
    return random.randint(1, sides)

def show_dice_face(value):
    faces = {
        1: "⚀", 2: "⚁", 3: "⚂",
        4: "⚃", 5: "⚄", 6: "⚅"
    }
    return faces.get(value, str(value))

def play_round(player_name, sides):
    guess = input(f"{player_name}, guess the dice roll (1-{sides}): ")
    if not guess.isdigit() or not 1 <= int(guess) <= sides:
        print("Invalid guess.")
        return 0
    roll = roll_dice(sides)
    print(f"🎲 Dice rolled: {show_dice_face(roll)}")
    return int(guess) == roll

def play_game():
    print("🎲 Welcome to the Advanced Dice Game!")
    player = input("Enter your name: ")
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
    sides = {"easy": 6, "medium": 12, "hard": 20}.get(difficulty, 6)
    rounds = 5
    score = 0

    for i in range(rounds):
        print(f"\n🔁 Round {i+1}")
        if play_round(player, sides):
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Missed!")

    print(f"\n🏁 Game Over! {player}'s score: {score}/{rounds}")

if __name__ == "__main__":
    play_game()
