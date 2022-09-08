"""A structured version of Wordle."""

__author__ = "730471791"

from re import L


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(initial_string: str, comparison_char: str) -> bool:
    """Returns True if the comparison character is found at any index of the initial string, and returns False otherwise."""
    assert len(comparison_char) == 1
    i: int = 0
    while i < len(initial_string):
        if initial_string[i] == comparison_char:
            return True
        i += 1
    return False

def emojified(guess: str, secret: str) -> str:
    """Return a string of emoji whose color indicates the accuracy of the users guess."""
    assert len(guess) == len(secret)
    emoji_string: str = ""
    counter: int = 0
    while counter < len(secret):
        if guess[counter] == secret[counter]:
            emoji_string += GREEN_BOX
        elif contains_char(secret, guess[counter]):
            emoji_string += YELLOW_BOX
        else:
            emoji_string += WHITE_BOX
        counter += 1
    return emoji_string

def input_guess(expected_length: int) -> str:
    """Returns the users guess with the proper length."""
    user_guess: str = input(f"Enter a {expected_length} character word: ")
    while len(user_guess) != expected_length:
        user_guess = input(f"That was not {expected_length} chars! Try again: ")
    return user_guess

def main() -> None:
    """The entry point of the program and main game loop."""
    secret_word: str = "codes"
    turn: int = 1
    has_won: bool = False
    while turn <= 6 and has_won == False:
        print(f"=== {turn}/6 ===")
        current_state: str = emojified(input_guess(len(secret_word)), secret_word)
        print(current_state)
        if current_state == GREEN_BOX * len(secret_word):
            has_won = True
            print(f"You won in {turn}/6 turns!")
        else:
            turn += 1
    if turn > 6:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()