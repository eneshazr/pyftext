import os
from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name="pyftext",
    version="1.1",
    description="Ascii Word Writing",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/yazilimfuryasi/pyftext",
    author="yazilimfuryasi@gmail.com",
    author_email="yazilimfuryasi@gmail.com",
    license="MIT",
    platforms="any",
    packages=find_packages(),
    python_requires=">=3.8.3",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
    include_package_data=True,
    install_requires=["Pillow"],
)

