import setuptools
from setuptools import setup


NAME = "news_api_backend"
VERSION = "0.1.0"
DESCRIPTION = "Really cool stuff"
URL = "https://www.google.com/"
AUTHOR = "half of northeastern cs4992 summer 2 2023"
AUTHOR_EMAIL = "furrier.t@northeastern.edu"
REQUIRES_PYTHON = ">=3.7.0"
REQUIRED = ["pandas", "requests>=2.0.0", "bs4", "fastapi", "uvicorn", "pydantic", "lxml", "scikit-learn",
            "textblob", "scikit-llm"]


DEV_REQUIRED = (
    REQUIRED
)

EXTRAS_REQUIRE = {
    "dev": DEV_REQUIRED,
}

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=setuptools.find_packages(include=["back_end", "back_end.*"]),
    install_requires=REQUIRED,
    extras_require=EXTRAS_REQUIRE,
    include_package_data=True,
    classifiers=["Programming Language :: Python :: 3"],
)
