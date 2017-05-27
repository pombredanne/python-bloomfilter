from io import BytesIO
import random
import tempfile

import pytest

from pybloom2.pybloom import BloomFilter, ScalableBloomFilter


TEST_SIZE = 12345


@pytest.mark.parametrize("file_class", [
    tempfile.TemporaryFile,
    BytesIO,
])
@pytest.mark.parametrize("filter_class,args", [
    (BloomFilter, (TEST_SIZE,)),
    (ScalableBloomFilter, ()),
])
def test_serialization(filter_class, args, file_class):
    expected = set([random.randint(0, 10000100) for _ in range(TEST_SIZE)])
    filter = filter_class(*args)
    for item in expected:
        filter.add(item)

    file_obj = file_class()
    filter.tofile(file_obj)

    del filter

    file_obj.seek(0)
    filter = filter_class.fromfile(file_obj)
    for item in expected:
        assert item in filter
    file_obj.close()
