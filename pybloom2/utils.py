from io import BytesIO


def is_bytes_io(instance):
    return isinstance(instance, BytesIO)
