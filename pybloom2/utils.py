from io import BytesIO


def is_string_io(instance):
    return isinstance(instance, BytesIO)
