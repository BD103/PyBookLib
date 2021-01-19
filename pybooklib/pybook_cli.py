import click

from pybooklib import console, pybook


@click.group()
def cli():
    "Request books and data from a specified library"
    pass

@cli.command()
@click.option("--user", default=None, help="Specific user")
@click.option("--book", default=None, help="Specific book / project")
@click.option("--version", default=None, help="Version of book")
@click.option("--direc", default=".", help="Directory to extract to")
def get(user, book, version, direc):
  "Umbrella get command that allows you to specify every detail"
  pybook.get(user=user, book=book, version=version, direc=direc)

@cli.command()
@click.argument("user")
@click.option("--direc", default=".", help="Directory to extract to")
def get_user(user, direc):
  "Gets all books from user and allows you to pick one"
  pybook.get(user=user, direc=direc)

@cli.command()
@click.argument("user")
@click.argument("book")
@click.option("--version", default=None, help="Version of book")
@click.option("--direc", default=".", help="Directory to extract to")
def get_book(user, book, version, direc):
  "Gets specific book from user"
  pybook.get(user=user, book=book, version=version, direc=direc)

@cli.command()
@click.argument("url")
def set_url(url):
  "Sets url to request books from"
  pybook.set_url(url=url)