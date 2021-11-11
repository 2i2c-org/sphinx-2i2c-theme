import nox

nox.options.reuse_existing_virtualenvs = True

build_command = ["-b", "html", "docs", "docs/_build/html"]

@nox.session
def docs(session):
    session.install("-e", ".[dev]")
    session.install("-r", "docs/requirements.txt")
    session.run("stb", "compile")
    session.run("sphinx-build", *build_command)

@nox.session(name="docs-live")
def docs_live(session):
    session.install("-e", ".[dev]")
    session.install("-r", "docs/requirements.txt")
    session.run("stb", "serve", "docs")
