"""A playful Gift. There's the G."""

__author__ = "Ranbir Pal"

input("Press enter to accept your sentence.")
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print("And Gsus wept, for none eternity separates a grain of sand.")
print("An infinity in an hour, a curse in your hand. ")
name: str = input("Prisoner, state thy name: ")
name = name + "G"
print()
print()
print()
print()
print()

print(f"Warden: Welcome {name}. Get comfy. The rest of your life will be spent in this while loop. You cannot escape.")
print(f"{name}: My name does not have an extra G at the end!]")
print(f"Sorry, {name}, we do not have to listen to prisoners. Go on now, at least the food is better than Chase Dining Hall.")
print(f"{name}: Yeah...")
print("The warden throws you into the prison and locks the door. You hear his laughter as he walks away.")
input("Press enter to continue. ")
print()
print()
print()

prison: bool = True
while prison:
    print("Options:")
    print("1. Eat prison food")
    print("2. Strange marks on the door.")
    print("3. Vent on the ceiling.")
    print("4. Look under the bed.")
    option: int = int(input("Please type the number of your choice: "))
    while option > 4 or option < 1:
        option = int(input("Please type a number between 1 and 4: "))





    prison = False

print("Freedom!")