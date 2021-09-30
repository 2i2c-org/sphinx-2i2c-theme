from setuptools import setup, find_packages
from pathlib import Path

lines = Path("sphinx_2i2c_theme").joinpath("__init__.py")
for line in lines.read_text().split("\n"):
    if line.startswith("__version__ ="):
        version = line.split(" = ")[-1].strip('"')
        break

setup(
    name="sphinx-2i2c-theme",
    version=version,
    python_requires=">=3.6",
    author="2i2c",
    author_email="hello@2i2c.org",
    project_urls={
        "Organization": "https://2i2c.org",
    },
    # this should be a whitespace separated string of keywords, not a list
    description="A lightweight theme for 2i2c",
    long_description=Path("./README.md").read_text(),
    long_description_content_type="text/markdown",
    license="BSD",
    packages=find_packages(),
    install_requires=[
        "sphinx-book-theme>=0.1.3",
    ],
    entry_points={"sphinx.html_themes": ["sphinx_2i2c_theme = sphinx_2i2c_theme"]},
    include_package_data=True,
)
