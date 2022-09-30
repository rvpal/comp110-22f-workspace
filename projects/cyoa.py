"""A choose your own adventure game."""

__author__ = "730471791"

from random import randint

points: int
player: str = ""
CAT: str = "\U0001F63E"
REWARD_SYMBOL: str = "\U0001F389"
MINUS_POINTS: str = "\U0001F4DB"
BLANK_LINE: str = "=================================================================="
has_cat_food: bool = False
cleaned_milk: bool = False
cat_relaxed: bool = False


def reward(change: int) -> None:
    """Updates the player on their points."""
    print(BLANK_LINE)
    global points
    points += change
    if change < 0:
        print(MINUS_POINTS)
        print(f"You have lost {points} skill.")
        print(f"Your cat skill-rating is {points}.")
        print(MINUS_POINTS)
    else:
        print(REWARD_SYMBOL)
        print(f"You have gained {points} skill.")
        print(f"Your cat skill-rating is {points}.")
        print(REWARD_SYMBOL)


def greet() -> None:
    """Welcomes the player and gets their name."""
    global player
    print(BLANK_LINE)
    player = input("Please input your name: ")
    print(f"Greetings {player}! This is a simple program. All you need to do is make a cat fall asleep.")
    print("I'll be judging you and determining your skill level based on your performance.")
    print("Right now the cat is wide awake and eager to cause trouble. Look at it:")
    print(CAT)
    print("Isn't it adorable? No, don't knock that glass of milk over! Ugh. Have fun...")
    

def feed() -> None:
    """Allows player to feed the cat if they have premium cat food and have cleaned the milk."""
    global points
    global cat_relaxed
    print(BLANK_LINE)
    print("You try to feed the cat.")
    if cleaned_milk:
        chosen: bool = False
        while not chosen:
            print(BLANK_LINE)
            print("1. Feed the cat plain cat food.")
            print("2. Feed the cat premium cat food.")
            selection = input("What do you want to do? Enter a number: ")
            if selection == "1" or selection == "2":
                chosen = True
            else:
                print("Please enter a valid choice.")
        if selection == "1":
            print(CAT)
            print(f"{player}, do you see that grumpy face? That cat refuses this bland cat food!")
            print("You fail!")
            reward(-20)
        elif selection == "2":
            if has_cat_food:
                print("You feed the cat the premium cat food.")
                print("The cat is now relaxed.")
                cat_relaxed = True
                print(CAT)
                print("Still looks grumpy though...")
                print(f"I would say, {player}, that this was an overall success!")
                reward(50)
            else:
                print("You do not have the premium cat food!")
                print(f"You cannot feed what you cannot have... {player}, I'm disappointed.")
                reward(-20)
    else:
        print("You have not cleaned the spilled milk!")
        print(CAT)
        print("The cat ignores your food and focuses on the milk.")
        reward(-20)


def pet(points: int) -> int:
    """Passes points and changes them."""
    global cat_relaxed
    print(BLANK_LINE)
    if cat_relaxed:
        print("You pet the cat and successfully make it fall asleep.")
        reset()
        return points + 30
    else:
        print(f"The cat is too energetic at the moment, {player}. You will need to fix that first.")
        print("I'm afraid this reflects poorly on your skill.")
        reward(-30)
        
        
def reset() -> None:
    """Resets all variables except points and player so that the game goes back to normal."""
    # Another cat walks in
    # The player is encouraged to increase their skill-rating.


def store() -> bool:
    """Allows the player to obtain cat food by working at a restaurant."""
    return True


def clean() -> bool:
    """Makes player clean milk."""
    print("You clean the milk.")
    return True


def main() -> None:
    """The entry point of the game."""
    greet()
    global points
    points = 0

    global cleaned_milk
    global has_cat_food
    selection: str = ""

    game_loop: bool = True
    while game_loop:
        chosen: bool = False
        while not chosen:
            print(BLANK_LINE)
            print("1. Feed the cat.")
            print("2. Pet the cat.")
            print("3. Go to the store.")
            if not cleaned_milk:
                print("4. Clean the milk.")
            print("5. Quit Game.")
            selection = input("What do you want to do? Enter a number: ")
            if selection == "1" or selection == "2" or selection == "3" or selection == "4" or selection == "5":
                chosen = True
            else:
                print("Please enter a valid choice.")
        if selection == "1":
            feed()
            chosen = False
        elif selection == "2":    
            points = pet(points)
            chosen = False
        elif selection == "3":
            has_cat_food = store()
            chosen = False
        elif selection == "4":
            cleaned_milk = clean()
            chosen = False
        elif selection == "5":
            print(BLANK_LINE)  
            print("Aw man! Well... I guess I can deal with this cat.")
            print("Thanks for stopping by.")
            quit()
        
    # Have a thing that compliments the player if their score is high enough. Encourage them to increase it when another cat walks in.


if __name__ == "__main__":
    main()