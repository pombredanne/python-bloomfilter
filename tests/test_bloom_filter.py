import random
import string

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


def test_error_rate():
    capacity = 1000
    error_rate = 0.01
    bf = BloomFilter(capacity=capacity, error_rate=error_rate)

    random_strings = []
    for _ in range(2 * capacity):
        length = random.randint(3, 9)
        random_string = "".join(random.choice(string.ascii_letters)
                                for _ in range(length))
        random_strings.append(random_string)

    strings_to_add = random_strings[:capacity]
    strings_to_check = random_strings[capacity:]

    for s in strings_to_add:
        bf.add(s)

    false_positives_count = 0
    for s in strings_to_check:
        if s in bf:
            false_positives_count += 1

    true_error_rate = false_positives_count / float(len(strings_to_check))

    assert true_error_rate <= 2 * error_rate
