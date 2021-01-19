import click

from pybooklib import console, pylib


@click.group()
def cli():
    "Host your own PyLib Server"
    pass


@cli.command()
def run():
    "Runs PyLib server"
    pylib.run()
