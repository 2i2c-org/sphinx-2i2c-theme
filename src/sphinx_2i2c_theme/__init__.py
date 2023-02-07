"""A lightweight theme for 2i2c."""
import os
from pathlib import Path
from sphinx_book_theme import hash_assets_for_files
from urllib.request import urlretrieve

__version__ = "0.0.1"

THEME_PATH = (Path(__file__).parent / "theme" / "sphinx-2i2c-theme").resolve()


def hash_html_assets(app, pagename, templatename, context, doctree):
    assets = ["styles/sphinx-2i2c-theme.css"]
    hash_assets_for_files(assets, THEME_PATH / "static", context)


def update_config(app):
    # Social previews config
    social_cards = app.config.ogp_social_cards
    if not social_cards:
        social_cards = {}

    # If no URL is set, don't generate social previews
    if not app.config.ogp_site_url:
        social_cards["site_url"] = "2i2c.org"

    # If no html_logo is set then use a stock 2i2c logo
    if not app.config.html_logo and not social_cards.get("image"):
        path_static = Path(__file__).parent / "theme/sphinx-2i2c-theme/static"
        path_img = path_static / "images/logo.png"
        social_cards["image"] = str(path_img)

    app.config.__dict__["ogp_social_cards"] = social_cards


def setup(app):
    app.connect("builder-inited", update_config)
    app.connect("html-page-context", hash_html_assets)
    
    app.add_html_theme("sphinx_2i2c_theme", THEME_PATH)
    app.config.html_favicon = "https://2i2c.org/media/icon.png"

    # Add the CSS for Fira, which we use in the logo
    path_css_out = str(Path(app.builder.outdir) / "_static" / "fira.css")
    urlretrieve("https://code.cdn.mozilla.net/fonts/fira.css", path_css_out)
    app.add_css_file("fira.css")

    # Activate a few extensions by default
    add_extensions = ["sphinx_copybutton", "sphinx_togglebutton", "sphinxext.opengraph"]
    for extension in add_extensions:
        app.setup_extension(extension)
