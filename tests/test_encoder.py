from typing import List, Tuple

import pytest
from hypothesis import example, given
from hypothesis import strategies as st

from encoder import decode, encode


# Example-based test for encode()
def test_encode_example() -> None:
    assert encode("yooooo") == [("y", 1), ("o", 5)]


# Example-based test for decode
def test_decode_example() -> None:
    assert decode([("y", 1), ("o", 5)]) == "yooooo"


# Example-based test for invertability property
def test_decode_inverts_encode_example() -> None:
    assert decode(encode("yooooo")) == "yooooo"


# Parameterized test to specify multiple examples and expected results
@pytest.mark.parametrize(
    ("input_plain_string", "expected_encoded"),
    [
        ("yooooo", [("y", 1), ("o", 5)]),
        ("hello", [("h", 1), ("e", 1), ("l", 2), ("o", 1)]),
        ("foo", [("f", 1), ("o", 2)]),
        ("bbbaar", [("b", 3), ("a", 2), ("r", 1)]),
        ("yyooww", [("y", 2), ("o", 2), ("w", 2)]),
    ],
)
def test_encode_parameterized(
    input_plain_string: str, expected_encoded: List[Tuple[str, int]]
) -> None:
    assert encode(input_plain_string) == expected_encoded


# Property-based test for invertability property
@given(s=st.text())
@example(s="")
def test_decode_inverts_encode_property(s: str) -> None:
    print(s)
    assert decode(encode(s)) == s


if __name__ == "__main__":
    pytest.main()
