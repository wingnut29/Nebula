from setuptools import setup, find_packages

packages = ['src']

with open("README.md") as readme:
    long_description = readme.read()

with open("requirements.txt") as requirements:
    install_requires = [line.strip() for line in requirements]

with open('resources/backend/version.txt', 'rt') as ver:
    VERSION = ver.read()

# with open('resources/backend/version.txt', 'w') as ver:
#     ver.write(VERSION)

setup(
    name='nebula',
    version=VERSION,
    packages=find_packages(),
    url='https://github.com/wingnut29/Nebula',
    license='MIT',
    author='Justin Mullins',
    author_email='jumullins@comcast.net',
    description='Study aid for advancement',
    long_description=long_description,
    install_requires=install_requires,
    include_package_data=True

)
