from encoder import encode, decode
import pytest
from hypothesis import given
from hypothesis.strategies import text
from typing import List, Tuple


@pytest.mark.skip
@given(text())
def test_decode_inverts_encode_property(s: str) -> None:
    assert decode(encode(s)) == s


def test_encode_example() -> None:
    assert encode("yooooo") == [("y", 1), ("o", 5)]


def test_decode_example() -> None:
    assert decode([("y", 1), ("o", 5)]) == "yooooo"


def test_decode_inverts_encode_example() -> None:
    assert decode(encode("yooooo")) == "yooooo"


@pytest.mark.parametrize(
    ("input_plain_string", "expected_encoded"),
    [
        ("yooooo", [("y", 1), ("o", 5)]),
    ],
)
def test_encode_parameterized(
    input_plain_string: str, expected_encoded: List[Tuple[str, int]]
) -> None:
    assert encode(input_plain_string) == expected_encoded


if __name__ == "__main__":
    pytest.main()
