import os

from setuptools import setup


NAME = "imgur_scraper"
DESCRIPTION = "Scrape years of Imgur's data without any authentication."
URL = "https://github.com/saadmanrafat/imgur-scraper"
EMAIL = "saadmanhere@gmail.com"
AUTHOR = "Saadman Rafat"
REQUIRES_PYTHON = ">=3.6.0"
VERSION = "0.1.14"
REQUIRED = ["requests-html", "requests"]

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name=NAME,
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=["imgur_scraper"],
    entry_points={
        "console_scripts": ["imgur-scraper=imgur_scraper.imgur_scraper:main"]
    },
    install_requires=REQUIRED,
    include_package_data=True,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy"
    ],
)
