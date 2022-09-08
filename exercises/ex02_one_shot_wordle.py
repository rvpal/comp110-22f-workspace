"""Exercise 02 - One-Shot Wordle - Loops!"""

__author__ = "730471791"

secret: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guess: str = input(f"What is your {len(secret)} letter guess? ")
while len(guess) != len(secret):
    guess = input(f"That was not {len(secret)} letters! Try again: ")

string: str = ""
i: int = 0
while i < len(guess):
    if guess[i] == secret[i]:
        string = string + GREEN_BOX
    else:
        boolean: bool = False
        j: int = 0
        while j < len(guess):
            if guess[i] == secret[j]:
                string = string + YELLOW_BOX
                boolean = True
            j = j + 1
        if not boolean:
            string = string + WHITE_BOX
    i = i + 1

print(string)
if string == GREEN_BOX * len(secret):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")