import os
from zipfile import ZipFile

import requests
from rich.progress import Progress
from rich.prompt import Prompt

from pybooklib import console


def pybook_init():
    if os.getenv("PYLIB_URL") is None:
        os.environ["PYLIB_URL"] = "https://pybooklib.bd103.repl.co/api"


def extract_book(r, direc):
    with open("tempbook.zip", "wb") as book:
        book.write(r.content)
    with ZipFile("tempbook.zip", "r") as book:
        if direc not in os.listdir():
            os.mkdir(direc)
        book.extractall(path=direc)
    os.remove("tempbook.zip")


def get(user=None, book=None, version=None, direc="."):
    with Progress() as progress:

        t_request = progress.add_task("Connecting to Server...", total=1, start=False)

        query = os.getenv("PYLIB_URL")

        if user is None:
            parameters = {}
        elif book is None:
            parameters = {"u": user}
        elif version is None:
            parameters = {"u": user, "b": book}
        else:
            parameters = {"u": user, "b": book, "v": version}

        r = requests.get(query, params=parameters)

        progress.start_task(t_request)
        progress.update(t_request, advance=1)

    if r.headers["Content-Type"] == "application/zip":
        extract_book(r, direc)
        console.log("[green]Finished book extraction.[/green]")
    elif r.headers["Content-Type"] == "application/json":
        data = r.json()
        if data["type"] == "User":
            if data["content"] != []:
                new_book = Prompt.ask(
                    "Enter book to download from " + user, choices=data["content"]
                )
                get(user, new_book, version=version, direc=direc)
            else:
                console.log("[red]BookError: User has no books.[/red]")
        elif data["type"] == "UserError":
            console.log("[red]UserError: " + data["content"] + "[/red]")
        elif data["type"] == "Book":
            console.log('[red]PyLibError: Returning deprecated "Book" type.[/red]')
        elif data["type"] == "BookError":
            console.log("[red]BookError: " + data["content"] + "[/red]")
        elif data["type"] == "Version":
            console.log('[red]PyLibError: Returning unused "Version" type.[/red]')
        elif data["type"] == "VersionError":
            console.log("[red]VersionError: " + data["content"] + "[/red]")
        else:
            console.log("[yellow]PyBookError: Error checking type.")
            console.log(data)
        console.log("[green]Finished JSON parse.[/green]")
    else:
        console.log("[red]Error: Content-Type is not json or zip![/red]")
