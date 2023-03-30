"""This is Wordle."""
__author__ = "730404725"

secret_word: str = "python"
word_guess: str = input("What is your 6-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
idx_guess: int = 0
emoji_guess: str = ("")
diff_idx: int = 0

while (len(word_guess) != len(secret_word)):
    word_guess = str(input("That was not 6 letters! Try again: "))
while idx_guess < len(secret_word):
    if word_guess[idx_guess] == secret_word[idx_guess]:
        emoji_guess = emoji_guess + GREEN_BOX
    else: 
        in_word: bool = False
        diff_idx = 0
        while in_word is False and (diff_idx < len(secret_word)):
            if secret_word[diff_idx] == word_guess[idx_guess]:
                in_word = True
            else: 
                diff_idx = diff_idx + 1
        if in_word is True:
            emoji_guess = emoji_guess + YELLOW_BOX
        else: 
            emoji_guess = emoji_guess + WHITE_BOX
    idx_guess = idx_guess + 1
print(emoji_guess)

if word_guess == secret_word:
    print("Woo! You got it!")
else: 
    if len(word_guess) == len(secret_word):
        print("Not quite. Play again soon!")
