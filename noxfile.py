import nox

nox.options.reuse_existing_virtualenvs = True

build_command = ["-b", "html", "docs", "docs/_build/html"]

@nox.session
def docs(session):
    session.install("-e", ".")
    session.install("-r", "docs/requirements.txt")
    session.run("sphinx-build", *build_command)

@nox.session(name="docs-live")
def docs_live(session):
    session.install("-e", ".")
    session.install("-r", "docs/requirements.txt")
    session.install("sphinx-autobuild")
    AUTOBUILD_IGNORE = [
        "_build",
        "build_assets",
    ]
    AUTOBUILD_WATCH = [
        "sphinx_2i2c_theme",
        "sphinx_2i2c_theme/static",
    ]
    cmd = ["sphinx-autobuild"]
    for folder in AUTOBUILD_IGNORE:
        cmd.extend(["--ignore", f"*/{folder}/*"])
    for folder in AUTOBUILD_WATCH:
        cmd.extend(["--watch", folder])
    cmd.extend(build_command)
    session.run(*cmd)
