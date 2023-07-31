from encoder import encode, decode
import pytest
from hypothesis import given
from hypothesis.strategies import text


@pytest.mark.skip
@given(text())
def test_decode_inverts_encode_property(s):
    assert decode(encode(s)) == s


def test_encode_example():
    assert encode("yooooo") == [("y", 1), ("o", 5)]


def test_decode_example():
    assert decode([("y", 1), ("o", 5)]) == "yooooo"


def test_decode_inverts_encode_example():
    assert decode(encode("yooooo")) == "yooooo"


@pytest.mark.parametrize(
    ("input_plain_string", "expected_encoded"),
    [
        ("yooooo", [("y", 1), ("o", 5)]),
    ],
)
def test_encode_parameterized(input_plain_string, expected_encoded):
    assert encode(input_plain_string) == expected_encoded


if __name__ == "__main__":
    pytest.main()
