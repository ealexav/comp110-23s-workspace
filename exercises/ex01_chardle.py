"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "230404725"

given_word: str = input("Enter a 5-character word: ")
given_letter: str = input("Enter a single character: ")

print("Searching for " + given_letter + " in " + given_word)

if(given_word[0] == given_letter):
    print(given_letter + " found at index 0")
else: 
    if(given_word[1] == given_letter):
        print(given_letter + " found at index 1")
    else:
        if(given_word[2] == given_letter):
            print(given_letter + " found at index 2") 
        else:
            if(given_word[3] == given_letter):
                print(given_letter + " found at index 3")
            else:
                if(given_word[4] == given_letter):
                    print(given_letter + " found at index 4")