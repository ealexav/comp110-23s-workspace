"""More list utils and practicing unit tests."""
__author__ = "730404725"


def only_evens(list_int: list[int]) -> list[int]:
    """Returning only evens in a given list."""
    even_num = []
    for n in list_int:
        if n % 2 == 0:
            even_num.append(n)
    return even_num

def concat(first: list[int], second: list[int]) -> list[int]:
    """Combining two lists into one."""
    outcome: list[int] = first + second
    return outcome

def sub(numbers: list[int], first_int: int, second_int: int) -> list[int]:
    """Returns a subset from a given list."""
    if first_int < 0:
        first_int = 0
    if second_int > len(numbers):
        second_int = len(numbers)
    subset: list[int] = []
    if len(numbers) == 0:
        return subset
    if first_int > len(numbers):
        return subset
    if second_int < 1:
        return subset
    while first_int < second_int:
        subset.append(numbers[first_int])
        first_int += 1
    return subset