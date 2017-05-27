import codecs
import os.path
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="pybloom2",
    use_scm_version={
        "root": here,
        "write_to": os.path.join(here, "pybloom2/_version.py"),
    },
    description="PyBloom2: A Probabilistic data structure",
    long_description=long_description,
    keywords=["data structures", "bloom filter", "bloom", "filter",
              "probabilistic", "set"],
    packages=["pybloom2"],
    platforms=["any"],
    zip_safe=True,

    author="Growbots",
    author_email="it@growbots.com",
    url="https://github.com/growbots/python-bloomfilter",
    license="MIT License",

    setup_requires=[
        "setuptools_scm>=1.10.1,<2.0.0",
    ],
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
