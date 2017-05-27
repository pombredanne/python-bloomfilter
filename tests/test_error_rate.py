import pytest

from pybloom2.pybloom import BloomFilter, ScalableBloomFilter
from tests.utils import get_random_string


CAPACITY = 1000
ERROR_RATE = 0.01


@pytest.mark.parametrize("filter_,acceptable_error_rate", [
    (BloomFilter(CAPACITY, ERROR_RATE), 2 * ERROR_RATE),
    (ScalableBloomFilter(5, ERROR_RATE), 1.1 * ERROR_RATE),
])
def test_error_rate(filter_, acceptable_error_rate):
    strings_to_add = set(get_random_string(3, 9) for _ in range(CAPACITY))
    strings_to_check = set(get_random_string(3, 9) for _ in range(CAPACITY))
    strings_to_check -= strings_to_add

    for s in strings_to_add:
        filter_.add(s)

    false_positives_count = 0
    for s in strings_to_check:
        if s in filter_:
            false_positives_count += 1

    true_error_rate = false_positives_count / len(strings_to_check)

    print(filter_.__class__.__name__, true_error_rate, acceptable_error_rate)
    assert true_error_rate <= acceptable_error_rate
