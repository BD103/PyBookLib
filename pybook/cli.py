import os

import click

import pybook


@click.group()
def cli():
    "Download and extract books from library"
    pass


@cli.command()
@click.argument("user")
@click.argument("book")
@click.option("--version", default=None, help="Book version, written in X.X.X format")
@click.option("--dir", default=".", help="Where to extract directory")
def get(user, book, version, dir):
    "Gets book from library and extracts code"
    pybook.get(user, book, version, dir)


@cli.command()
@click.argument("url")
def set_url(url):
    "Sets URL of library"
    pybook.set_environ(url)
