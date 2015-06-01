# coding: utf-8

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

base_path = os.path.dirname(__FILE__)
requirements_path = os.path.join(base_path, "requirements.txt")
long_description_path = os.path.join(base_path, "README.md")
version_path = os.path.join(base_path, "rpcblockchainexplorer/__init__.py")

# dependency list is loaded later
requires = []

# version is also loaded later
version = None

def __filter_requirements(requirements):
    """
    Remove lines that are not related to requirements.
    """
    return [line for line in requirements if line[0] != "#"]

def __get_version(version_content):
    """
    Extract the version number from the `__init__.py` file.
    """
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        version_content,
        re.MULTILINE,
    ).group(1)

    if not version:
        raise Exception("Cannot find version information.")

    return version

with open(requirements_path, "r") as requirements_file:
    requirements = requirements_file.read()
    requirements = requirements.split("\n")
    requires = __filter_requirements(requirements)

with open(long_description_path, "r") as readme_file:
    long_description = readme_file.read()

with open(version_path, "r") as version_file:
    content = version_file.read()
    version = __get_version(content)

setup(
    # metadata
    name="rpcblockchainexplorer",
    version=version,
    url="https://github.com/kanzure/rpcblockchainexplorer",
    license="BSD",

    # details
    description="Lightweight local RPC blockchain explorer (web application)",
    long_description=long_description,
    install_requires=requires,

    # blame who?
    author="Bryan Bishop",
    author_email="kanzure@gmail.com",

    # just being conservative here..
    zip_safe=False,

    # for the greater good
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
    ]
)
