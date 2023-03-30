"""Example function for unit tests"""

def sum(xs: list[float]) -> float:
    """return the sum of all elements in xs"""
    sum_total: float = 0.0
    idx: int = 0
    for num in xs:
        sum_total += num
    return sum_total