"""Dictionaries function skeletons."""

__author__ = "730404725"

def invert(existing_dict: dict[str, str]) -> dict[str, str]:
    """Keys and values switching in dict. """
    resulting_dict: dict[str, str] = {}
    for k, v in resulting_dict.items():
        resulting_dict[v] = k
    return resulting_dict

def favorite_color(fav_color: dict[str, str]) -> str:
    """Most common colors in dictionary."""
    resulting_dict: dict[str, int] = {}
    for v in fav_color:
        if fav_color[v] in resulting_dict:
            resulting_dict[fav_color[v]] = 0
        else:
            resulting_dict[fav_color[v]] +=1 
    return resulting_dict

def count(existing_list: list[str]) -> dict[str, int]:
    """Counting how many elements in a list."""
    new_dict: dict[str, int] = {}
    for x in existing_list:
        if x in new_dict:
            new_dict[x] += 1
        else:
            new_dict[x] = 1
        return new_dict
