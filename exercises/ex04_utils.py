"""Working on List Utility Functions."""
__author__ = "730404725"

def all(list_num: list[int], diff_number:int) -> bool:
    """list of ints returning bool"""
    if len(list_num) == 0:
        return False
    idx_list: int = 0
    while idx_list < len(list_num):
        if list_num[idx_list] != diff_number:
            return False
        else:
            idx_list += 1
    return True
        
def max(input: list[int]) -> int:
    """This will return the longest int in the list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    idx_input: int = 0
    max_number: int = input[0]
    while idx_input < len(input):
        if input[idx_input] > max_number:
            max_number = input[idx_input]
        idx_input += 1
    return max_number

def is_equal(first: list[int], second: list[int]) -> bool:
    """2 lists will return a bool"""
    idx_equal: int = 0
    if len(first) != len(second):
            return False
    while idx_equal < (len(first) and len(second)):  
        if first[idx_equal] != second[idx_equal]:
            return False
    idx_equal += 1
    return True