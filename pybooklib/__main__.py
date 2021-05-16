import click


@click.group()
def cli():
  pass


@cli.command()
@click.option(
  "-p", "--pypi", "location",
  flag_value="pypi", help="ID is PyPI Package, default.")
@click.option(
  "-g", "--github", "location",
  flag_value="github", help="ID is Github repo.")
@click.option(
  "-gr", "--github-release", "location",
  flag_value="github_release", help="ID is Github release.")
@click.option(
  "-w", "--web", "location",
  flag_value="web", help="ID is internet link.")
@click.option(
  "-f", "--file", "location",
  flag_value="file", help="ID is local file.")
@click.argument("id")
def pbl(id, location="pypi"):
  """Executes script from ID.

  ID is where to find the script.
  """
  print(location, id)


if __name__ == "__main__":
  cli()
