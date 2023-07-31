"""encoder.py

Run-length encoder.
"""

from typing import List, Tuple


def encode(input_string: str) -> List[Tuple[str, int]]:
    """Encode a string into a run-length encoded collection.
    Example
    >>> assert encode("yooooo") == [('y', 1), ('o', 5)]
    """

    if not input_string:
        return []

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
    """Decode a run-length encoded collection into a string.

    Example
    >>> assert decode([('y', 1), ('o', 5)]) == "yooooo"
    """
    q = ""
    for character, count in lst:
        q += character * count
    return q
