import click
from rich.markdown import Markdown

from pybooklib import console, data

try:
    import importlib.resources as pkg_resources
except ImportError:
    # For Python < 3.7
    import importlib_resources as pkg_resources


@click.command()
def about():
    "Get information of PyBookLib"
    text = pkg_resources.read_text(data, "about.md")
    console.print(Markdown(text))
