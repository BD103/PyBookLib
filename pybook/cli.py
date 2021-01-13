import os

import click

import pybook


@click.group()
def cli():
    "Download / Upload Python Projects"
    pass


@cli.command()
@click.argument("user")
@click.argument("project")
def get(user, project):
    pass


# @TODO Update and move cmd
@cli.command()
@click.argument("url")
def set_url(url):
    pybook.set_environ(url)
