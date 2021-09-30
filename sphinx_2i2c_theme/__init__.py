"""A lightweight theme for 2i2c."""
import os
from pathlib import Path

__version__ = "0.0.1"

def setup(app):
    path_theme = os.path.abspath(Path(__file__).parent)
    app.add_html_theme("sphinx_2i2c_theme", path_theme)
    app.add_css_file("https://code.cdn.mozilla.net/fonts/fira.css")
