from setuptools import setup, find_packages

setup(
    name="canonical-assesment",  # Name of the package
    version="0.1",  # Project version
    packages=find_packages(where="src"),  # Tell setuptools to find packages under src
    package_dir={"": "src"},  # Treat src as the directory where packages are found
)