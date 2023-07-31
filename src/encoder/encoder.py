"""encoder.py

Run-length encoder.
"""

from typing import List, Tuple


def encode(input_string: str) -> List[Tuple[str, int]]:
    """Example
    >>> assert encode("yooooo") == [('y', 1), ('o', 5)]
    """
    count = 1
    prev = ""
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    entry = (character, count)
    lst.append(entry)
    return lst


def decode(lst: List[Tuple[str, int]]) -> str:
    """Example
    >>> decode([('y', 1), ('o', 5)]) == "yooooo"
    """
    q = ""
    for character, count in lst:
        q += character * count
    return q
