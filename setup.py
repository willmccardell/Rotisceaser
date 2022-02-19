#!/usr/bin/env python

from setuptools import find_packages, setup

test_deps = [
    "coverage",
    "pytest",
    "flake8",
]

setup(
    name="rotisceaser",
    version="1.0.0",
    description="My First Package!",
    python_requires='>3.9',
    install_requires= [
        'click ~= 8.0.3',
        'click-log ~= 0.3.2',
        'requests ~= 2.27',
    ],
    tests_require=test_deps,
    extras_require={
        "test": test_deps,
    },
    packages=find_packages(),
    include_package_data=True,
    # PIP uses this to install your script as an executable
    # if you pip install, you can then call it with "hello_python" and that's it!
    entry_points={
        "console_scripts": [
            "rotisceaser = rotisceaser.main:main",
        ],
    },
)