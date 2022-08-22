"""An example of conditional if/else statements."""

SECRET: int = 3

print("I'm thinking of a number between one and five. What is it? ")
guess: int = int(input("What is your guess? "))

if guess == SECRET: 
    print("You guessed correctly!")
    print("Have a wonderful day!")
else: 
    print("Sorry. That is incorrect.")
    if guess > SECRET:
        print("You guessed too high!")
    else:
        print("You guessed to low!")

print("Game Over.")