# This file is used to setup our projects and their dependencies

import setuptools

# Writing README file for our package
with open("README.md", "r", encoding= 'utf-8') as f:
    long_description = f.read()
    
__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "loobiish"
SRC_REPO = "textSummarizer"     # Name in our config folder
AUTHOR_EMAIL = "kumar.lavish.0109@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/loobiish/Text-Summarizer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

