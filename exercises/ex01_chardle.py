"""Exercise 01: A simple version of Wordle - Chardle."""

__author__ = "730471791"

from ssl import SSLObject


word: str = str(input("Enter a 5-character word: "))
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

char: str = str(input("Enter a single character: "))
if len(char) != 1:
    print("Error: Character must be a single character")
    exit()

print("Searching for " + char + " in " + word)

total: int = 0

if char == word[0]:
    print(char + " found at index 0")
    total = total + 1
if char == word[1]:
    print(char + " found at index 1")
    total = total + 1
if char == word[2]:
    print(char + " found at index 2")
    total = total + 1
if char == word[3]:
    print(char + " found at index 3")
    total = total + 1
if char == word[4]:
    print(char + " found at index 4")
    total = total + 1

if total == 0:
    print("No instances of " + char + " found in " + word)
if total == 1:
    print("1 instance of " + char + " found in " + word)
else:
    print(str(total) + " instances of " + char + " found in " + word)