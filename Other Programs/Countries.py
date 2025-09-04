country = "Spain"

print("In this program you will need to guess the country I am thinking of")
print("I am thinking of a country between London and Japan")

while True:
    guess = input("Enter your guess: ")

    if guess == "UK":
        print("That's not right :(")

    elif guess == "Poland":
        print("That's not right :(")

    elif guess == "Spain":
        print("Your guess is correct!!")
        break

    else:
        print("Interesting guess, but not quite!")
