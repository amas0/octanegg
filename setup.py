from pathlib import Path
from setuptools import setup, find_packages

readme_path = Path(__file__).parent / 'README.md'

with open(readme_path, 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(name='octanegg',
      version='1.0.1',
      author='amas0',
      author_email='andrew.mascioli1@gmail.com',
      description='Python client library for octane.gg public API',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/amas0/octanegg',
      packages=find_packages(),
      install_requires=[
            'requests'
      ],
      python_requires='>=3.7')
