from encoder import encode, decode
import pytest


def test_encode():
    assert encode("yooooo") == [("y", 1), ("o", 5)]


def test_decode():
    assert decode([("y", 1), ("o", 5)]) == "yooooo"


def test_encode_decode_reversability():
    assert decode(encode("yooooo")) == "yooooo"


if __name__ == "__main__":
    pytest.main()
