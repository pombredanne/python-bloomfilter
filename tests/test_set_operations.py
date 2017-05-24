import pytest

from pybloom2.pybloom import BloomFilter, ScalableBloomFilter


def test_union():
    bloom_one = BloomFilter(100, 0.001)
    bloom_two = BloomFilter(100, 0.001)
    chars = [chr(i) for i in range(97, 123)]

    for char in chars[int(len(chars)/2):]:
        bloom_one.add(char)

    for char in chars[:int(len(chars)/2)]:
        bloom_two.add(char)

    new_bloom = bloom_one.union(bloom_two)

    for char in chars:
        assert char in new_bloom


def test_intersection():
    bloom_one = BloomFilter(100, 0.001)
    bloom_two = BloomFilter(100, 0.001)

    chars = [chr(i) for i in range(97, 123)]

    for char in chars:
        bloom_one.add(char)

    for char in chars[:int(len(chars)/2)]:
        bloom_two.add(char)

    new_bloom = bloom_one.intersection(bloom_two)

    for char in chars[:int(len(chars)/2)]:
        assert char in new_bloom

    for char in chars[int(len(chars)/2):]:
        assert char not in new_bloom


def test_intersection_capacity_fail():
    bloom_one = BloomFilter(1000, 0.001)
    bloom_two = BloomFilter(100, 0.001)

    with pytest.raises(ValueError):
        bloom_one.intersection(bloom_two)


def test_union_capacity_fail():
    bloom_one = BloomFilter(1000, 0.001)
    bloom_two = BloomFilter(100, 0.001)

    with pytest.raises(ValueError):
        bloom_one.union(bloom_two)


def test_intersection_k_fail():
    bloom_one = BloomFilter(100, 0.001)
    bloom_two = BloomFilter(100, 0.01)

    with pytest.raises(ValueError):
        bloom_one.intersection(bloom_two)


def test_union_k_fail():
    bloom_one = BloomFilter(100, 0.01)
    bloom_two = BloomFilter(100, 0.001)

    with pytest.raises(ValueError):
        bloom_one.union(bloom_two)
