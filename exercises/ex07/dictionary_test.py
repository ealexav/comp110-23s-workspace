"""Dictionaries testing."""

__author__ = "730404725"

from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count

def test_invert_empty() -> None:
    """Testing an empty dictionary."""
    assert invert() == dict()

def test_invert_normal() -> None:
    """Testing for inverted dictionaries."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}

def test_invert_repeat() -> None:
    """Testing for repeated values."""
    assert invert({'kris': 'jordan', 'michael': 'jordan'}) == KeyError

def test_favorite_color() -> None:
    """Testing for common favorite color."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"})

def test_favorite_color() -> None:
    """Favorite color on an empty dictionary."""
    assert favorite_color({}) == ""

def test_favorite_color_tie() -> None:
    """Testing if there is a tie between colors."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Sarah": "yellow"})

def test_count_empty() -> None:
    """Testing the count of an empty list."""
    assert count({}) == {}

def test_count_normal() -> None:
    """Testing one item enetered."""
    assert count ({"1", "2", "3", "4"}) == {"1": 1, "2": 1, "3": 1, "4": 1}

def test_count_repeated() -> None:
    """Testinf repeating items in a list."""
    assert count({"1", "2", "1", "2", "3"}) == {"1": 2, "2": 2, "3": 1}