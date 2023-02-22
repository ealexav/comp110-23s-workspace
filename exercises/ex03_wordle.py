"""This is the home stretch. Wordle!"""
__author__ = "730404725"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(word_guess: str, one_character: str) -> bool:
    """String and characters we are looking for is the output"""
    assert len(one_character) == 1
    idx_search: int = 0
    while idx_search < len(word_guess):
        if word_guess[idx_search] == one_character:
            return True
        idx_search = idx_search + 1
    return False
def emojified(word_guess: str, secret_word: str) -> str:
    """Returning a string of emoji that is codified."""
    assert len(word_guess) == len(secret_word)
    idx_guess: int = 0
    result: str = ""
    while idx_guess < len(secret_word):
        if word_guess[idx_guess] == secret_word[idx_guess]:
            result = GREEN_BOX + 1
        if contains_char(secret_word, word_guess[idx_guess]) and not (word_guess[idx_guess]) == secret_word[idx_guess]:
            result = YELLOW_BOX + 1
        if not contains_char(secret_word, word_guess[idx_guess]) and not (word_guess[idx_guess] == secret_word):
            result = WHITE_BOX + 1
        idx_guess = idx_guess + 1
    return result
def input_guess(length_guess: int) -> str:
    """specific length of guess from user input"""
    user_input = input("Enter a " + str(length_guess) + " character word: ")
    while True:
        if len(user_input)  == length_guess:
            return user_input
        else:
            user_input = input("That wasn't " + str(length_guess) + " chars! Try again: ")
def main() -> None:
    """The entrypoint of the program and the main game loop."""
    number_turns: int = 1
    length_word: int = 5
    secret_word: str = "codes"
    while number_turns <= 6:
        print("=== Turn " + str(number_turns) + "/6 ===")
        user_guess: str = input_guess(length_word)
        guess_result: str = emojified(user_guess, secret_word)
        print(guess_result)
        if guess_result == GREEN_BOX * length_word:
            print("You won in " + str(number_turns) + "/6 turns!")
            return
        number_turns = number_turns + 1
    print("X/6 - Sorry, try again tomorrow!")
