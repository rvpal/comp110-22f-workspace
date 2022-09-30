"""A choose your own adventure game."""

__author__ = "730471791"

from random import randint

points: int
player: str
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
    print(points)
    points += change
    if change < 0:
        print(MINUS_POINTS)
        print(f"You have lost {-change} skill.")
        print(f"Your cat skill-rating is {points}.")
        print(MINUS_POINTS)
    else:
        print(REWARD_SYMBOL)
        print(f"You have gained {change} skill.")
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
        print("The cat ignores your food and focuses on drinking the milk instead.")
        reward(-20)


def pet(points: int) -> int:
    """Passes points and changes them."""
    global cat_relaxed
    print(BLANK_LINE)
    if cat_relaxed:
        print("You pet the cat and successfully make it fall asleep.")
        print(REWARD_SYMBOL)
        print("You have gained 30 skill.")
        print(f"Your cat skill-rating is {points + 30}.")
        print(REWARD_SYMBOL)
        reset()
        return points + 30
    else:
        print(f"The cat is too energetic at the moment, {player}. You will need to fix that first.")
        print("I'm afraid this reflects poorly on your skill.")
        print(REWARD_SYMBOL)
        print("You have lost 30 skill.")
        print(f"Your cat skill-rating is {points - 30}.")
        print(REWARD_SYMBOL)
        return points - 30
        
        
def reset() -> None:
    """Resets all variables except points and player so that the game goes back to normal."""
    global has_cat_food
    global cat_relaxed
    global cleaned_milk
    print(BLANK_LINE)
    has_cat_food = False
    cat_relaxed = False
    cleaned_milk = False
    print(f"I must say, {player}, you have exceeded my expectations.")
    print(f"And keep in mind, you finished with a skill level of {points}, so that tells you what my expectations for you were...")
    print("Now, I have an unlimited supply of cats, so if you want your score to be even better, then you can keep playing!")
    print("Here is another cat:")
    print(CAT)
    print(f"Golly, {player}! The cat has already knocked over another glass of milk.")
    print("Better get to it!")
    input("Press enter to restart the game (you'll keep your skill-rating, though).")
    print(BLANK_LINE)


def store() -> bool:
    """Allows the player to obtain cat food by working at a restaurant."""
    print(BLANK_LINE)
    print(f"You enter the store. What did you want to buy here, {player}?")
    money: int = 0
    chosen: bool = False
    store_loop: bool = True
    while store_loop:
        while not chosen:
            print(BLANK_LINE)
            print("1. Buy premium cat food.")
            print("2. Work at the restaurant.")
            selection = input("What do you want to do? Enter a number: ")
            if selection == "1" or selection == "2":
                chosen = True
            else:
                print("Please enter a valid choice.")
        if selection == "1":
            if money >= 100:
                print("You successfully buy the premium cat food.")
                print(f"{player}: Why was it so expensive!?!?!")
                print("Now now, you need a positive attitude if you want to take care of a cat.")
                reward(25)
                return True
            else:
                print(f"Sorry, {player}, you do not have enough money to buy the cat food.")
                print("A responsible cat owner should keep track of their finances.")
                reward(-10)
                print("Perhaps you should work at the restaurant.")
            chosen = False
        elif selection == "2":    
            print("You leave the store and go work a four hour shift at some random restaurant.")
            print(f"This, {player}, is quite smart. With the labor shortage it is easy to find a job.")
            print("All you need are good tips and hopefully you can make some money.")
            print("YOU WORK A FOUR HOUR SHIFT")
            money += randint(40, 50)
            print(f"You earned 40 dollars from working and {money - 40} in tips.")
            print(f"You now have {money} dollars!")
            print("You may need to work another shift...")
            reward(5)
            chosen = False


def clean() -> bool:
    """Makes player clean milk."""
    print("It was something worth crying over, so you clean the spilled milk.")
    reward(15)
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
            if not cat_relaxed:
                print("1. Feed the cat.")
            print("2. Pet the cat.")
            if not has_cat_food:
                print("3. Go to the store.")
            if not cleaned_milk:
                print("4. Clean the milk.")
            print("5. Quit Game.")
            selection = input("What do you want to do? Enter a number: ")
            if (selection == "1" and not cat_relaxed) or selection == "2" or (selection == "3" and not has_cat_food) or (selection == "4" and not cleaned_milk) or selection == "5":
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


if __name__ == "__main__":
    main()