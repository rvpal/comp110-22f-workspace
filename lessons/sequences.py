"""Examples of the tuple and range sequences."""

# An example of a tuple without type aliasing. 
goat: tuple[str, int] = ("MJ", 23)

# Tuples are sequences, so they're 0-indexed.
print(goat[0])
print(goat[1])

# Printing a typle produces its literal syntax. 
print(goat)

# Sequences have lengths.
print(len(goat))

# Sequences are iterable with for... in loops. 
for item in goat:
    print(item)

# Tuples, unlike lists, are immutable.
# goat[0] = "LBJ"
# This gives an error.

# We can "invent" our own type with a type alias (CamelCasing is the naming convention)
Player = tuple[str, int]

# Once we've aliased a type, we can create variables of that type.
unc_player_of_the_year: Player = ("Bacot", 5)

# In a strange world where jersey numbers chance...
unc_player_of_the_year = (unc_player_of_the_year[0], unc_player_of_the_year[1] + 1)
# A bit tedious since it is so hard to chance a tuple. 


# A range is another common sequence type. 
zero_to_nine: range = range(0, 10, 1)

# We can access items of the range. 
print(zero_to_nine[0])
print(zero_to_nine[9])

# A range is iterable.
for i in zero_to_nine:
    print(i)

# We can have different steps for more control. 
odds_to_99: range = range(1, 100, 2)

for i in odds_to_99:
    print(i)

# 0 is a very common starting value and 1 is a common stepping value. 
# Thus, range(10) is equivalent to range(0, 10, 1)

# BIG USE OF RANGE:
names: list[str] = ["Kris", "Logan", "Michael", "Gsus", "Ranbir", "Pal", "Joyner", "COMP", "Class"]
for i in range(len(names)):
    print(f"{i}, {names[i]}")

# Useful if we want to iterate over a list without needing to step by 1 necessarily.
for i in range(0, len(names), 2):
    print(f"{i}, {names[i]}")

# Attributes:
print(odds_to_99.stop) # prints the stopping value (100) of odds_to_99. The stopping value is an attribute of a range. 