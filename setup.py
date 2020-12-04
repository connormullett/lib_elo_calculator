#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
  name="lib_elo_calculator",
  packages=find_packages(include=['lib_elo_calculator']),
  version='0.1.0',
  description='contains functions and formulas for calculating elo',
  author='Connor Mullett',
  license='MIT',
  setup_requires=['pytest-runner'],
  tests_require=['pytest'],
  test_suite='tests'
)

