"""Setup configuration for sailorsuperstitions."""

from setuptools import find_packages, setup

setup(
    name="sailorsuperstitions",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "sailorsuperstitions": ["data/*.json"],
    },
    python_requires=">=3.8",
    author="Seth Clark",
    author_email="caradoxical@gmail.com",
    description="A package to check sailing conditions against maritime superstitions",
)
