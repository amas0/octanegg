from setuptools import setup, find_packages

setup(name='octanegg',
      version='0.1',
      author='amas0',
      description='Python client library for octane.gg public API',
      packages=find_packages(),
      install_requires=[
            'requests'
      ])
