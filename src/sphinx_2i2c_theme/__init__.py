"""A lightweight theme for 2i2c."""
import os
from pathlib import Path
from sphinx_book_theme import hash_assets_for_files
from sphinx.util import logging
from .video import Video

__version__ = "0.0.1"
LOGGER = logging.getLogger(__name__)

THEME_PATH = (Path(__file__).parent / "theme" / "sphinx-2i2c-theme").resolve()

def update_config(app, config):
    # Social previews config
    social_cards = config.ogp_social_cards
    if not social_cards:
        social_cards = {}

    # If no URL is set, don't generate social previews
    if not config.ogp_site_url:
        social_cards["site_url"] = "2i2c.org"

    # If no html_logo is set then use a stock 2i2c logo
    if not config.html_logo and not social_cards.get("image"):
        path_static = Path(__file__).parent / "theme/sphinx-2i2c-theme/static"
        path_img = path_static / "images/logo.png"
        social_cards["image"] = str(path_img)

    config.__dict__["ogp_social_cards"] = social_cards
    config.__dict__["theme_in_extensions"] = True


def check_theme_in_extensions(app):
    if not hasattr(app.config, "theme_in_extensions"):
        LOGGER.warn(("'sphinx_2i2c_theme' is not in Sphinx extensions list. ""Some features will be missing."))


def hash_html_assets(app, pagename, templatename, context, doctree):
    assets = ["styles/sphinx-2i2c-theme.css"]
    hash_assets_for_files(assets, THEME_PATH / "static", context)


def setup(app):
    app.add_html_theme("sphinx_2i2c_theme", THEME_PATH)
    app.config.html_favicon = "https://2i2c.org/media/icon.png"
    app.connect("config-inited", update_config)
    app.connect("builder-inited", check_theme_in_extensions)
    app.connect("html-page-context", hash_html_assets)

    # Link to the Mozilla CDN because downloading locally doesn't seem to work
    app.add_css_file("vendor/fira.css")

    # Activate a few extensions by default
    add_extensions = ["sphinx_copybutton", "sphinx_togglebutton", "sphinxext.opengraph", "sphinx.ext.intersphinx"]
    for extension in add_extensions:
        app.setup_extension(extension)

    # Video directive
    app.add_directive("video", Video)
