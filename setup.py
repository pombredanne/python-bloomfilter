#!/usr/bin/env python
from setuptools import setup


VERSION = "2.0.0"
DESCRIPTION = "PyBloom2: A Probabilistic data structure"
LONG_DESCRIPTION = """
pybloom2 is a Python implementation of the bloom filter probabilistic data
structure. The module also provides a Scalable Bloom Filter that allows a
bloom filter to grow without knowing the original set size.
"""


setup(
    name="pybloom2",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    keywords=("data structures", "bloom filter", "bloom", "filter",
              "probabilistic", "set"),
    packages=["pybloom2"],
    platforms=["any"],
    zip_safe=True,

    author="Growbots",
    url="https://github.com/growbots/python-bloomfilter",
    license="MIT License",

    install_requires=[
        "bitarray>=0.3.4",
    ],
    extras_require={
        "tests": [
            "flake8",
            "pytest",
            "pytest-flake8",
        ],
    },
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",

        "Topic :: Utilities",
        "Topic :: Database :: Database Engines/Servers",
        "Topic :: Software Development :: Libraries :: Python Modules",

        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
    ]
)
