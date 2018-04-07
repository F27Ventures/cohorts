from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='f27_cohorts',
    version='1.0.0',
    description='Make cohort analysis a magical experience',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/F27Ventures/cohorts',
    license='MIT',
    author='F27 Ventures',
    author_email='dev@f27.ventures',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='python cohort analysis daa-science startups',
    packages=find_packages(),
    setup_requires=['setuptools>=38.6.0']
)