import click
from pybooklib import console
from rich.markdown import Markdown
from . import data
try:
    import importlib.resources as pkg_resources
except ImportError:
    # For Python < 3.7
    import importlib_resources as pkg_resources


@click.command()
def about():
  text = pkg_resources.read_text(data, "about.md")
  console.print(Markdown(text))