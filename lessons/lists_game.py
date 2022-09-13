"""Examples of using lists in a single 'game.'."""

from random import randint

# example: list[int] = list() # Sets up an emty list of integers.
# example.append(1) # Method call.
# example.append(3)
# example.append("Jeff")
# print(example)
# print(len(example))

rolls: list[int] = list()
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# print(rolls[0])
# print(rolls[1])

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))

print(rolls)

rolls.pop(len(rolls) - 1)
print(rolls)

i: int = 0
sum: int = 0
while i < len(rolls):
    sum += rolls[i]
    i += 1

print(f'Total Score: {sum}')