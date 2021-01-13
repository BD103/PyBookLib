import click

import pylib


@click.group()
def cli():
    "Host your own PyLib Server"
    pass


@cli.command()
def run():
    pylib.run()
