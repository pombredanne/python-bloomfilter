import random
import string


def get_random_string(min_len, max_len):
    """Return string of random chars of length between min_len and max_len"""
    length = random.randint(min_len, max_len)
    return "".join(random.choice(string.ascii_letters)
                   for _ in range(length))
