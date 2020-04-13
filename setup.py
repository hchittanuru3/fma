import os
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='freemusicarchive',
      version='0.0.0',
      description='Free Music Archive',
      url='https://github.com/mdeff/fma',
      author='Michaël Defferrard',
      author_email='michael.defferrard@epfl.ch',
      install_requires = required,
      packages=['fma'],
      license='MIT')
