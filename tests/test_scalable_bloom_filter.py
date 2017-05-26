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
