"""A lightweight theme for 2i2c."""
import os
from pathlib import Path
from sphinx_book_theme import hash_assets_for_files

__version__ = "0.0.1"

THEME_PATH = (Path(__file__).parent / "theme" / "sphinx-2i2c-theme").resolve()

def hash_html_assets(app, pagename, templatename, context, doctree):
    assets = ["styles/sphinx-2i2c-theme.css"]
    hash_assets_for_files(assets, THEME_PATH / "static", context)

def update_config(app):
    # Social previews config
    social_previews = app.config.ogp_social_previews
    if not social_previews:
        social_previews = {}

    # If no URL is set, don't generate social previews
    if not app.config.ogp_site_url:
        social_previews["site_url"] = "2i2c.org"

    # If no html_logo is set then use a stock 2i2c logo
    if not app.config.html_logo and not social_previews.get("image"):
        path_static = Path(__file__).parent / "theme/sphinx-2i2c-theme/static"
        path_img = path_static / "images/logo.png"
        social_previews["image"] = str(path_img)

    app.config.__dict__["ogp_social_previews"] = social_previews

def setup(app):
    app.add_html_theme("sphinx_2i2c_theme", THEME_PATH)
    app.add_css_file("https://code.cdn.mozilla.net/fonts/fira.css")
    app.config.html_favicon = "https://2i2c.org/media/icon.png"
    app.connect("builder-inited", update_config)
    app.connect("html-page-context", hash_html_assets)

    # Activate a few extensions by default
    add_extensions = ["sphinx_copybutton", "sphinx_togglebutton", "sphinxext.opengraph", "sphinx_social_previews"]
    for extension in add_extensions:
        app.setup_extension(extension)
