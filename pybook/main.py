import os

import requests


def init():
    if os.getenv("PYBOOK_URL") is None:
        os.environ["PYBOOK_URL"] = "https://pybooklib.bd103.repl.co/api"


def get(user, project):
    r = requests.get(os.getenv("PYBOOK_URL"))


def set_environ(url):
    os.environ["PYBOOK_URL"] = url
