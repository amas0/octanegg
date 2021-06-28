from setuptools import setup, find_packages

setup(name='octanegg',
      version='1.0',
      author='amas0',
      author_email='andrew.mascioli1@gmail.com',
      description='Python client library for octane.gg public API',
      url='https://github.com/amas0/octanegg',
      packages=find_packages(),
      install_requires=[
            'requests'
      ],
      python_requires='>=3.7')
