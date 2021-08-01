from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.5'
DESCRIPTION = 'Python library based on C++ to show Windows 10 based toast notification. '
LONG_DESCRIPTION = 'A pure python module based on C++ to show toast notification in Windows 10 Operating System.'

# Setting up
setup(
    name="Toast4Windows",
    version=VERSION,
    author="Pankaj Pande",
    author_email="pkjpande@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['winrt'],
    keywords=['python', 'windows toast', 'toast', 'notifications', 'windows notifications', 'windows popup'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)