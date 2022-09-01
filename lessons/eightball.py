"""Random integers and elif statements."""

__author__ = "730471791"

from random import randint

question: str = input("What is your yes/no question? ")
response: int = randint(0, 3)

if response == 0:
    print("Yes, def.")
elif response == 1:
    print("Ask again later.")
elif response == 2:
    print("My sources say no.")
else:
    print("Nope.")