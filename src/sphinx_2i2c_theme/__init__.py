"""A lightweight theme for 2i2c."""
import os
from pathlib import Path
from sphinx_book_theme import hash_assets_for_files

__version__ = "0.0.1"

THEME_PATH = (Path(__file__).parent / "theme" / "sphinx-2i2c-theme").resolve()

def hash_html_assets(app, pagename, templatename, context, doctree):
    assets = ["styles/sphinx-2i2c-theme.css"]
    hash_assets_for_files(assets, THEME_PATH / "static", context)

def setup(app):
    app.add_html_theme("sphinx_2i2c_theme", THEME_PATH)
    app.add_css_file("https://code.cdn.mozilla.net/fonts/fira.css")
    app.config.html_favicon = "https://2i2c.org/media/icon.png"
    app.connect("html-page-context", hash_html_assets)
