"""Snakes and Ladders - Two Player Games!"""
import random

turns = 0
player1_square = 0
player2_square = 0

print('Welcome to Snakes and Ladders the GAME')
print('You need to reach square 80 to win!')

while player1_square < 80 and player2_square < 80:
    # Player 1 turn
    print('Player 1 press enter to roll the dice')
    input()
    dice_roll = random.randint(1, 6)
    print(f'You rolled a {dice_roll}')
    player1_square += dice_roll

    print()
    
    # Player 2 turn
    print('Player 2 press enter to roll the dice')
    input()
    dice_roll = random.randint(1, 6)
    print(f'You rolled a {dice_roll}')
    player2_square += dice_roll
    
    turns += 1
    
    # Player 1 - Ladders
    if player1_square in [5, 12, 19, 24, 27, 32, 40, 45, 68]:
        ladder_roll = random.randint(1, 14)
        print('Player 1 landed on a ladder!')
        print(f'Player 1 moved {ladder_roll} squares')
        print()
        player1_square += ladder_roll
    
    # Player 1 - Snakes
    if player1_square in [12, 15, 23, 24, 33, 39, 48, 49]:
        snake_roll = random.randint(1, 12)
        print('Player 1 landed on a snake!')
        print(f'Player 1 moved back {snake_roll} squares')
        print()
        player1_square -= snake_roll

    # Player 2 - Ladders
    if player2_square in [5, 12, 19, 24, 27, 32, 40, 45]:
        ladder_roll = random.randint(1, 14)
        print('Player 2 landed on a ladder!')
        print(f'Player 2 moved {ladder_roll} squares')
        print()
        player2_square += ladder_roll
    
    # Player 2 - Snakes
    if player2_square in [12, 15, 23, 24, 33, 39, 48, 49, 79]:
        snake_roll = random.randint(1, 12)
        print('Player 2 landed on a snake!')
        print(f'Player 2 moved back {snake_roll} squares')
        print()
        player2_square -= snake_roll
        
    print(f'Player 1 is on square {player1_square}')
    print(f'Player 2 is on square {player2_square}')
    print()
    
# Determine winner
if player1_square > player2_square:
    print('🏆 Player 1 Wins!')
elif player2_square > player1_square:
    print('🏆 Player 2 Wins!')
else:
    print("It's a Tie! Better luck next time.")

print(f'That took {turns} turns')
