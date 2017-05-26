import random
import string

import pytest

from pybloom2.pybloom import ScalableBloomFilter


def test_init():
    with pytest.raises(ValueError):
        ScalableBloomFilter(error_rate=0)


def test_add():
    sbf = ScalableBloomFilter()

    assert "test" not in sbf
    assert "test2" not in sbf

    assert not sbf.add("test")

    assert "test" in sbf
    assert "test2" not in sbf

    assert not sbf.add("test2")
    assert "test" in sbf
    assert "test2" in sbf

    assert sbf.add("test")
    assert sbf.add("test2")
    assert "test" in sbf
    assert "test2" in sbf


def test_len():
    sbf = ScalableBloomFilter(initial_capacity=1)

    assert len(sbf) == 0

    sbf.add("test")

    assert len(sbf) == 1

    sbf.add("test2")

    assert len(sbf) == 2


def test_capacity():
    initial_capacity = 5
    sbf = ScalableBloomFilter(initial_capacity=initial_capacity)

    for i in range(initial_capacity):
        sbf.add(i)

    sbf.add(initial_capacity)

    assert len(sbf) == sbf.count == initial_capacity + 1


def test_multiple_bloom_filters():
    initial_capacity = 5
    test_size = 100 * initial_capacity
    sbf = ScalableBloomFilter(initial_capacity=initial_capacity)

    for i in range(test_size):
        sbf.add(i)

    assert len(sbf) == sbf.count == test_size

    for i in range(test_size):
        assert i in sbf


def test_error_rate():
    test_size = 1000
    error_rate = 0.01
    sbf = ScalableBloomFilter(initial_capacity=5, error_rate=error_rate)

    random_strings = []
    for _ in range(2 * test_size):
        length = random.randint(3, 9)
        random_string = "".join(random.choice(string.ascii_letters)
                                for _ in range(length))
        random_strings.append(random_string)

    strings_to_add = random_strings[:test_size]
    strings_to_check = random_strings[test_size:]

    for s in strings_to_add:
        sbf.add(s)

    false_positives_count = 0
    for s in strings_to_check:
        if s in sbf:
            false_positives_count += 1

    true_error_rate = false_positives_count / float(len(strings_to_check))

    assert true_error_rate <= error_rate
