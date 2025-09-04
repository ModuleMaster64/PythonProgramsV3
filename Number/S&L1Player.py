import random
Squares = 0
print('Welcome to the Snakes and Ladders The GAME!')
print('You must reach 100 to win the game')
while Squares < 101:
    print('Roll the dice by pressing enter')
    input()
    DiceRoll = random.randint(1,6)
    print('You rolled a',DiceRoll)
    Squares = Squares + DiceRoll
    Squares = str(Squares)
    print('You are on Square' + Squares)
    Squares = int(Squares)
    if Squares == 8:
        print('Well done, go up the ladder to square 23')
        Squares = Squares + 15
    if Squares ==10:
        print('Oh no, you have landed on a snake,go back five')
        Squares = Squares - 5
    if Squares ==54:
        print('Well done, go up the ladder to square 60')
        Squares = Squares + 60
    if Squares ==15:
        print('Oh no, you have landed on a snake, go down 5 squares')
        Squares = Squares - 5
    if Squares ==24:
        print('Well done, go up the ladder to square 29')
        Squares = Squares + 5
    if Squares ==30:
        print('Oh no, you have landed on a snake go down 8 spaces')
        Squares = Squares - 8
    if Squares ==21:
        print('Well done, go up the ladder to square 23')
        Squares = Squares + 2
    if Squares ==31:
        print('Oh no, you have landed on a snake, go down five spaces')
        Squares = Squares - 5
    if Squares ==63:
        print('Oh no, you have landed on the biggest snake')
        Squares = Squares - 60
