import pytest

from pybloom2.pybloom import BloomFilter


def test_init():
    with pytest.raises(ValueError):
        BloomFilter(capacity=1000, error_rate=0)

    with pytest.raises(ValueError):
        BloomFilter(capacity=0)


def test_add():
    bf = BloomFilter(capacity=1000)

    assert "test" not in bf
    assert "test2" not in bf

    bf.add("test")
    assert "test" in bf
    assert "test2" not in bf

    bf.add("test2")
    assert "test" in bf
    assert "test2" in bf


def test_len():
    bf = BloomFilter(capacity=1000)

    assert len(bf) == 0

    bf.add("test")
    bf.add("test2")

    assert len(bf) == 2


def test_capacity():
    bf = BloomFilter(capacity=100)

    for i in range(100):
        bf.add(i)

    with pytest.raises(IndexError):
        bf.add(100)
