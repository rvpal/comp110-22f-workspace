"""A choose your own adventure game!"""

__author__ = "730471791"

from random import randint

EMOJI_GUIDE: str = "\U0001F610"
THE_VILLAIN: str = f"{EMOJI_GUIDE} Guide"
REWARD_SYMBOL: str = "\U0001F389"
ZERO_POINTS: str = "\U0001F4DB"
ACTION_SYMBOL: str = "\U00002B55"
BLANK_LINE: str = "=================================================================="
points: int
player: str
loop: int = 0
has_food: bool = False


def reward(change: int) -> None:
    """Updates the player on their points."""
    global points
    points += change
    if points <= 0:
        print(ZERO_POINTS)
        print(f"You have {points} ponts.")
        print(ZERO_POINTS)
    else:
        print(REWARD_SYMBOL)
        print(f"You have {points} points.")
        print(REWARD_SYMBOL)


def greet() -> None:
    """Introduces the game and names the player."""
    global player
    print(BLANK_LINE)
    print("A FATE SO HORRID")
    print(BLANK_LINE)
    print(f"{ACTION_SYMBOL} An incredible amount of pain courses through your body. The very air seems hostile to you.")
    print(f"{ACTION_SYMBOL} This dark cavern torments you. You want nothing more than to leave this place. But how will you get out?")
    if points <= 0:
        print(f"{THE_VILLAIN}: Ah. You suffer from your pitiful lack of point. Thus, by grace, to you five I will anoint.")
        reward(5)
    print(f"{THE_VILLAIN}: Indeed, adventure points are what it seeks. But can it face that which reeks?")
    player = input("Fallen one, your name is your own. For eternity inscribe it in stone: ")
    print(f"{ACTION_SYMBOL} You dip your hands in something infernal and depress into a copper plate your adamantine identity.")
    print(f"{THE_VILLAIN}: {player}, let your need for points propell you forward, lest you meet a fate so horrid.")
    print(BLANK_LINE)


def gate() -> bool:
    """Returns True if the player has enough points to open the gate, or false if otherwise."""
    print(BLANK_LINE)
    print(f"{ACTION_SYMBOL} You go down one end of the cavern, uphill. You see a faint glimmer of light. But a gate blocks your path.")
    print(f"{ACTION_SYMBOL} There is some writing on the gate: ")
    print("A LARGE AMOUNT OF POINTS I REQUIRE FOR ONE SOUL TO PASS.")
    input("Press enter to offer your points.")
    print()
    if points >= 100:
        print(f"{ACTION_SYMBOL} You stand before the gate and offer your points.")
        print(f"{ACTION_SYMBOL} You feel a rumbling in your stomach as the points start to leave you to open the gate.")
        print(f"{ACTION_SYMBOL} Suddenly, the guide intercepts you. He starts scooping up the points for himself.")
        print(f"{THE_VILLAIN}: A mighty amount of points art thine. Though now they shalt be mine!")
        return True
    else:
        print(f"{ACTION_SYMBOL} You stand before the gate and offer your adventure points. Nothing happens.")
        print(f"{THE_VILLAIN}: Adventure points you lack, thus you should go back.")
        print(BLANK_LINE)
        return False


def escape() -> None:
    print(BLANK_LINE)
    punishment: int = points * -1
    reward(punishment)
    print(f"{THE_VILLAIN} *Over the top evil laughter*. Ever more, suffer hereafter.")
    print(f"{ACTION_SYMBOL} The guide passes through the gate, but you are unable to follow. He has stolen your adventure points.")
    print(f"{ACTION_SYMBOL} This creator has *truly* made the greatest plot-twist of all time. Shakespeare is shaking.")
    print(f"{ACTION_SYMBOL} The gate is once again closed. It reads the same as before.")
    print("A LARGE AMOUNT OF POINTS I REQUIRE FOR ONE SOUL TO PASS.")
    print(f"{ACTION_SYMBOL} The pool of dark liquid starts bubbling. A ghastly person rises from the liquified computer screens.")


def explore(event: int) -> int:
    """Provides the paths for the 3 random events from the explore the cavern option. Returns an amount of adventure points."""
    print(BLANK_LINE)
    global has_food
    if event == 1:
        print(f"{ACTION_SYMBOL} You come across a pool of black liquid.")
        print(f"{player}: is that... ink?")
        print(f"{THE_VILLAIN}: They are liquified computer screens from a previous comp-sci student. A student who was not so prudent.")
        print(f"{ACTION_SYMBOL} The dark liquid starts to bubble madly. Out from the liquid a rabbit appears. It has red eyes and sharp fangs.")
        print(f"{ACTION_SYMBOL} What will you do?")
        options: list[str] = ["1. Fight the rabbit", "2. Feed the rabbit."]
        selection: str = ""
        while selection != "1" and selection != "2":
            for option in options:
                print(option)
            selection = input("Select a choice (type the number): ")
            if selection != "1" and selection != "2":
                print(f"{THE_VILLAIN} Something valid must you select, if you will a choice elect!")
        if selection == "1":
            success: int = randint(1, 2)
            if success == 1:
                print(f"{ACTION_SYMBOL} You successfully defeat the rabbit.")
                return 15
            elif success == 2:
                print(f"{ACTION_SYMBOL} The rabbit is too powerful for you to handle.") 
                print("Its fangs almost plunge into you, but you manage to run to another part of the cave.") 
                print("The rabbit gets bored and goes back into the pool of liquidized computer screens.")
                return 10
        elif selection == "2":
            if has_food:
                print(f"{ACTION_SYMBOL} You give the rabbit the rotten flesh you found. It feasts on its former companion.")
                print(f"{ACTION_SYMBOL} The rabbit, now full, goes back into the liquidized pool of computer screens.")
                print(f"{THE_VILLAIN}: It is futile to resist the world's rule, even if nature is often cruel.")
                has_food = False
                return 25
            else:
                print(f"{ACTION_SYMBOL} You have no food to give!")
                print(f"{ACTION_SYMBOL} The rabbit lunges at you: you manage to get away luckily.")
                print(f"{THE_VILLAIN}: Why would you try to feed without food. That's like building a treehouse without wood.")
                return 5
    elif event == 2:
        print(f"{ACTION_SYMBOL} You find some rotten flesh on the ground. It appears to be rabbit-shaped.")
        has_food = True
        return 5
    elif event == 3: 
        print("TEST EXPLORE EVENT 3")
        # event 3: return some int
        return 0


def main() -> None:
    """The entrypoint of the game."""
    global points
    global player
    global loop
    points = 0
    reward(0)
    greet()
    
    ultra_loop: bool = True
    while ultra_loop:
        if loop > 0:
            reward(0)

        print(f"{THE_VILLAIN}: So. You wish to leave this place and escape your fate. I understand, perhaps you shall try the gate.")
        print(f"{ACTION_SYMBOL} What will you do?")
        choices: list[str] = ["1. Try the gate", "2. Explore the cavern", "3. Quit game"]
        trapped: bool = True

        while trapped:
            selection: str = ""
            while selection != "1" and selection != "2" and selection != "3":
                for choice in choices:
                    print(choice)
                selection = input("Select a choice (type the number): ")
                if selection != "1" and selection != "2" and selection != "3":
                    print(f"{THE_VILLAIN} Something valid must you select, if you will a choice elect!")
            if selection == "1":
                if gate():
                    trapped = False
            elif selection == "2":
                random_event: int = randint(1, 3)
                reward(explore(random_event))
            elif selection == "3":
                print(BLANK_LINE)
                print(f"{THE_VILLAIN}: Quit this game if you must, for in your will I cannot trust.")
                quit()
        escape()
        loop += 1


if __name__ == "__main__":
    main()