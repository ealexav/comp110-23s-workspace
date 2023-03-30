"""A Buzzfeed quiz(maybe)."""

__author__ = "730404725"

player: str = ""
points: int
answer: list[str] = []
QUIZ_RESULT: str = "\U0001F7E9"

def main() -> None:
    """Beginning of the quiz."""
    global points
    points = 0
    greet()
    print(quiz())
    print(result(100))

def greet() -> None:
    """The quiz greets the player."""
    global player
    player  = input("What is your preferred name? ")
    print(f"{player}, what is your favorite color?" )

def result(points: int) -> int:
    """How many points lead to a result."""
    if points == 100:
        print("Total points: ")
    return points

def quiz() -> str:
    """Quiz will be completed."""
    print("#1 What color is your room?: ")
    question_1: str = input(f"{player}: red, blue, yellow, green")
    if len(question_1) > 0:
        global points
        points += 25
        global result
        answer.append(question_1)
        print(f"Points: {points}/100")
    print("#2 What color is your car?")
    question_2: str = input(f"red, blue, green, yellow")
    if len(question_2) > 0:
        points += 25
        answer.append(question_2)
        print(f"Pints: {points}/100")
    print("#3 What color is your bracelet?")
    question_3: str = input(f"red, blue, green, yellow")
    if len(question_3) > 0:
        points += 25
        answer.append(question_3)
        print(f"Points: {points}/100")
    print("#3 What color is your shirt?")
    question_4: str = input(f"red, blue, green, yellow")
    if len(question_4) > 0:
        points += 25
        answer.append(question_4)
        print(f"Points: {points}/100")
    color: str = ""
    result: list[str] = ["red", "green", "blue", "yellow", "purple"]
    import random
    color += random.choice(result)
    f_answer: str = f"Your favorite color is {color}" + QUIZ_RESULT + "!"
    return f_answer

if __name__ == "__main__":
    main()