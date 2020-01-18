from setuptools import setup, find_packages

with open("README.md","r") as fh:
    long_description = fh.read()

setup(
    name= "example-pkg-andre_rangel",
    version= "0.1",
    author= "André Rangel Vieira",
    author_email= "rangel_andre@outlook.com",
    description= "An example package",
    long_description= long_description,
    long_description_content_type= "text/markdown",
    url= "https://github.com/pypa/sampleproject",
    packages=find_packages(),
    classifiers= [
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires= '>=3.6'
)

