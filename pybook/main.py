import os
from getch import getch
import requests
import json


def init():
    if os.getenv("PYBOOK_URL") is None:
        os.environ["PYBOOK_URL"] = "https://pybooklib.bd103.repl.co/api"


def load(book):
    pass


def gen_pick_book(books, selected):
    for i in len(books):
        print("\033[A", end="")
    for i in len(books):
        if i == selected:
            print("\033[37m" + books[i] + "\033[39m")
        else:
            print("\033[34m" + books[i] + "\033[39m")


def pick_book(books):
    selected = 0
    picking = True
    while picking:
        gen_pick_book(books, selected)
        key = getch()
        if key == "\033[A" and selected > 0:
            selected -= 1
        elif key == "\033[B" and selected < len(books):
            selected += 1
        elif key == "\n":
            picking = False
    return books[selected]


def get(user, book, version, dir):
    if version is None:
        params = {"u": user, "b": book}
    else:
        params = {"u": user, "b": book, "v": version}
    r = requests.get(os.getenv("PYBOOK_URL"), params=params)
    response = r.json()
    if response["type"] == "Book":
        load(response["content"])
    elif response["type"] == "BookError":
        print("BookError:", response["content"])
    elif response["type"] == "User":
        pick_book(response["content"])
    elif response["type"] == "UserError":
        print("UserError:", response["content"])
    else:
        print(
            "UnknownTypeError: Please open up an issue on Github at github.com/BD103/PyBookLib/issues with the content of stream.txt"
        )
        with open("stream.txt", "rt") as stream:
            print(response, file=stream)


def set_environ(url):
    os.environ["PYBOOK_URL"] = url
