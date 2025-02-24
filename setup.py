import os

from setuptools import find_packages
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


requirements = read("requirements.txt").split()


setup(
    name="syft-tensorflow",
    version="0.0.0a0",
    author="OpenMined",
    author_email="contact@openmined.org",
    description=("TensorFlow Bindings for PySyft"),
    license="Apache-2.0",
    keywords="deep learning artificial intelligence privacy secure " +
             "multi-party computation federated learning differential privacy",
    packages=find_packages(exclude=["docs", "examples", "dist"]),
    include_package_data=True,
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/OpenMined/PySyft-TensorFlow",
    install_requires=requirements,
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-flake8"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
