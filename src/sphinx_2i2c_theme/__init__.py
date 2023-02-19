"""A lightweight theme for 2i2c."""
import os
from pathlib import Path
from sphinx_book_theme import hash_assets_for_files
from sphinx.util import logging
from .video import Video

__version__ = "0.0.1"
LOGGER = logging.getLogger(__name__)

THEME_PATH = (Path(__file__).parent / "theme" / "sphinx-2i2c-theme").resolve()


def _config_provided_by_user(app, key):
    """Check if the user has manually provided the config.
    REMOVE when pydata v0.14 is released and import from there.
    """
    return any(key in ii for ii in [app.config.overrides, app.config._raw_config])


def update_config(app):
    # If no URL is set, don't generate social previews
    if not _config_provided_by_user(app, "ogp_site_url"):
        app.config.ogp_site_url = "2i2c.org"

    # Social previews config
    social_cards = app.config.__dict__.get("ogp_social_cards", {})

    # If no html_logo is set then use a stock 2i2c logo
    if not _config_provided_by_user(app, "html_logo") and not social_cards.get("image"):
        path_static = Path(__file__).parent / "theme/sphinx-2i2c-theme/static"
        path_img = path_static / "images/logo.png"
        social_cards["image"] = str(path_img)

    app.config.ogp_social_cards = social_cards


def hash_html_assets(app, pagename, templatename, context, doctree):
    assets = ["styles/sphinx-2i2c-theme.css"]
    hash_assets_for_files(assets, THEME_PATH / "static", context)


def setup(app):
    app.add_html_theme("sphinx_2i2c_theme", THEME_PATH)
    app.config.html_favicon = "https://2i2c.org/media/icon.png"
    app.connect("builder-inited", update_config)
    app.connect("html-page-context", hash_html_assets)

    # Add our folder for templates
    here = Path(__file__).parent.resolve()
    theme_path = here / "theme" / "sphinx-2i2c-theme"
    app.config.templates_path.append(str(theme_path / "components"))

    # Link to the Mozilla CDN because downloading locally doesn't seem to work
    app.add_css_file("https://fonts.cdnfonts.com/css/fira-sans-book")

    # Remove all of the `config-inited` event listeners because they've already triggered
    # We'll then re-trigger this event after adding extensions so that *only* their event hooks trigger
    app.events.listeners["config-inited"] = []

    # Activate a few extensions by default
    add_extensions = ["sphinx_copybutton", "sphinx_togglebutton", "sphinxext.opengraph", "sphinx.ext.intersphinx"]
    for extension in add_extensions:
        app.setup_extension(extension)

    # Emit the two events that have already happened
    # This ensures that any newly-loaded extensions that were listening for these
    # events are triggered.
    app.emit("config-inited", app.config)

    # Video directive
    app.add_directive("video", Video)
