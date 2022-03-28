from setuptools import setup, find_packages

setup(
    name = 'pysimpleig',
    version = '1.0.0',
    description = 'A library to help simplifying the usage instagram',
    author = 'novitae',
    url = 'https://github.com/novitae/PySimpleIG',
    classifiers = [
        'Programming Language :: Python :: 3.9',
    ],
    packages = find_packages(),
    install_requires = ["requests"],
)
