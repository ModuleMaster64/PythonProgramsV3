import random

turns=0
squares1=0
squares2=0

print('Welcome to Snakes and Ladders the GAME')
print('You need to reach square 80 to win!')

while squares1 < 80 and squares2 < 80:
    print('Player 1 press enter to roll the dice')
    input()
    diceroll=random.randint(1,6)
    print('You rolled a', diceroll)
    squares1 += diceroll

    print()
    
    print('Player 2 press enter to roll the dice')
    input()
    diceroll=random.randint(1,6)
    print('You rolled a', diceroll)
    squares2 += diceroll
    
    turns += 1
    
    if squares1 == 5 or squares1 == 12 or squares1 == 19 or squares1 == 24 or squares1 == 27 or squares1 == 32 or squares1 == 40 or squares1 == 45 or squares1 == 68:
        ladderroll = random.randint(1,14)
        print('Player 1 landed on a ladder!')
        print('Player 1 moved', str(ladderroll), ' squares')
        print()
        squares1 += ladderroll
    if squares1 == 12 or squares1 == 15 or squares1 == 23 or squares1 == 24 or squares1 == 33 or squares1 == 39 or squares1 == 48 or squares1 == 49:
        snakeroll = random.randint(1,12)
        print('Player 1 landed on a snake!')
        print('Player 1 moved back', snakeroll,'squares')
        print()
        squares1 -= snakeroll

    if squares2 == 5 or squares2 == 12 or squares2 == 19 or squares2 == 24 or squares2 == 27 or squares2 == 32 or squares2 == 40 or squares2 == 45:
        ladderroll = random.randint(1,14)
        print('Player 2 landed on a ladder!')
        print('Player 2 moved', str(ladderroll), ' squares')
        print()
        squares2 += ladderroll
    if squares2 == 12 or squares2 == 15 or squares2 == 23 or squares2 == 24 or squares2 == 33 or squares2 == 39 or squares2 == 48 or squares2 == 49 or squares1 == 79:
        snakeroll = random.randint(1,12)
        print('Player 2 landed on a snake!')
        print('Player 2 moved back', snakeroll,'squares')
        print()
        squares2 -= snakeroll
        
    print('Player 1 is on square', str(squares1))
    print('Player 2 is on square', str(squares2))
    print()
    
if squares1 > squares2:
    print('Player 1 Wins!')
if squares2 > squares1:
    print('Player 2 Wins!')
if squares1 == squares2:
    print('It\'s a Tie! Better luck next time.')

print('That took', turns,'turns')
