from setuptools import setup, find_packages

with open("../README.md") as readme:
    long_description = readme.read()

with open("../requirements.txt") as requirements:
    install_requires = [line.strip() for line in requirements]

setup(
    name='Nebula',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/wingnut29/Nebula',
    license='MIT',
    author='Justin Mullins',
    author_email='',
    description='',
    long_description=long_description,
    install_requires=install_requires
)
