"""A few notes on While loops."""

counter: int = 0
maximum: int = int(input("Count up to what? Please enter a number: "))
while counter <= maximum:
    counter_squared: int = counter ** 2
    print(str(counter) + " - The square of " + str(counter) + " is " + str(counter_squared))
    counter += 1

print("Done!")

"""Looping through a string."""
print("Part 2:")

string: str = input("Give me a string: ")

# i is a common counting variable name. 
# i is short for iteration.
i: int = 0

while i < len(string):
    print(string[i])
    i = i + 1