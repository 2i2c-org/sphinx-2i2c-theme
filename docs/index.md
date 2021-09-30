# The 2i2c documentation theme

A lightweight theme built on the Sphinx Book Theme, for use by 2i2c.

```{toctree}
:maxdepth: 3
reference/kitchen-sink/index
```

## Theme structure

This theme tries to make minimal changes to the `sphinx-book-theme` in order to standardize a top-bar that can be shared across all 2i2c documentation.

It does these two primary things:

- Overrides the `layout.html` template so that we include a topbar of links
- Adds some CSS that standardizes the look and feel according to 2i2c colors

## Build the theme locally

You can build the documentation for this theme to preview it.
The easiest way to build the documentation in this repository is to use [the `nox` automation tool](https://nox.thea.codes/), a tool for quickly building environments and running commands within them.
This ensures that your environment has all the dependencies needed to build the documentation.

To do so, follow these steps:

1. Install `nox`

   ```console
   $ pip install nox
   ```
2. Build the documentation:

   ```console
   $ nox -s docs_build
   ```

This should create a local environment in a `.nox` folder, build the documentation (as specified in the `noxfile.py` configuration), and the output will be in `docs/_build/html`.

To build live documentation that updates when you update local files, run the following command:

```console
$ nox -s docs_live
```
