"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "230404725"

given_word: str = input("Enter a 5-character word: ")
if (len(given_word) != 5):
    print("Error: Word must contain 5 characters")
    exit()
given_letter: str = input("Enter a single character: ")
if (len(given_letter) != 1):
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + given_letter + " in " + given_word)

instance = 0

if (given_word[0] == given_letter):
    print(given_letter + " found at index 0")
    instance = instance + 1
if (given_word[1] == given_letter):
    print(given_letter + " found at index 1")
    instance = instance + 1
if (given_word[2] == given_letter):
    print(given_letter + " found at index 2") 
    instance = instance + 1
if (given_word[3] == given_letter):
    print(given_letter + " found at index 3")
    instance = instance + 1
if (given_word[4] == given_letter):
    print(given_letter + " found at index 4")
    instance = instance + 1


if (instance == 0):
    print("No instances of " + given_letter + " found in " + given_word)
if (instance == 1):
    print("1 instance of " + given_letter + " found in " + given_word)
if (instance == 2):
    print("2 instances of " + given_letter + " found in " + given_word)
if (instance == 3):
    print("3 instances of " + given_letter + " found in " + given_word)
if (instance == 4):
    print("4 instances of " + given_letter + " found in " + given_word)
if (instance == 5):
    print("5 instances of " + given_letter + " found in " + given_word)
