import setuptools
from get_github_description import get_github_description
from __version__ import __version__
import os

pkg_name = os.environ['PKG_NAME']
author = "umihico"
author_email = "umihico@users.noreply.github.com"
github_url = "https://github.com/umihico/pypienv"
description = get_github_description(github_url)
python_requires = '>=3.7'
requirements = [
    'requests',
    'boto3',
]

with open("README.md", "r") as f:
    long_description = f.read()
setuptools.setup(
    name=pkg_name,
    version=__version__,
    author=author,
    author_email=author_email,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=github_url,
    packages=[pkg_name.replace("-", "_")],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=python_requires,
)
