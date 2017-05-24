from io import BytesIO
import random
import tempfile

import pytest

from pybloom2.pybloom import BloomFilter, ScalableBloomFilter


TEST_SIZE = 12345


@pytest.mark.parametrize("klass,args", [
    (BloomFilter, (TEST_SIZE,)),
    (ScalableBloomFilter, ()),
])
def test_serialization(klass, args):
    expected = set([random.randint(0, 10000100) for _ in range(TEST_SIZE)])
    filter = klass(*args)
    for item in expected:
        filter.add(item)

    f = tempfile.TemporaryFile()
    filter.tofile(f)
    bytesio = BytesIO()
    filter.tofile(bytesio)
    streams_to_test = [f, bytesio]

    del filter

    for stream in streams_to_test:
        stream.seek(0)
        filter = klass.fromfile(stream)
        for item in expected:
            assert item in filter
        del(filter)
        stream.close()
