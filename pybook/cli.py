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


@cli.command()
@click.argument("url")
def set_url(url):
    pybook.host.set_environ(url)


# @TODO: REMOVE
@cli.command()
def run():
    pybook.host.run()
