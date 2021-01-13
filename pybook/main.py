import os

import requests


def init():
    if os.getenv("PYBOOK_URL") is None:
        os.environ["PYBOOK_URL"] = "https://pybook.bd103.repl.co/api/{user}/{project}"


def get(user, project):
    r = requests.get(os.getenv("PYBOOK_URL").format(user=user, project=project))
