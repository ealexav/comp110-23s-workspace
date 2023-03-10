"""running unit tests"""

__author__ = "730404725"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat

def test_only_evens_empty() -> None:
    """empty list test"""
    assert only_evens([]) == []
def test_only_evens() -> None:
    """testing for only evens"""
    assert only_evens([2, 4, 6]) == [2, 4, 6]
def test_only_evens_everything() -> None:
    """tests eveyrthing in a list for evens"""
    assert only_evens([1, 2, 3]) == [2]

def test_concat_empty() -> None:
    """testing the combining of two empty lists"""
    assert concat([], []) == []
def test_concat_lists() -> None:
    """combining two lists that contain elements"""
    assert concat([1, 2], [3, 4]) == [1, 2, 3, 4]
def test_concat_different_lengths() -> None:
    """combining two lists of different lengths"""
    assert concat([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]

def test_sub_empty() -> None:
    """testing empty list"""
    num = []
    assert sub[num, 1, 4] == []
def test_sub_negative() -> None:
    """testing for negative start"""
    numbers = [1, 2, 3]
    assert sub(numbers, -1, -2) == [1, 2]
def test_sub_idx_difference() -> None:
    """testing is the end index is greater than length of list"""
    numbers = [1, 2, 3]
    assert sub(numbers, 1, 6) == [2, 3, 4]