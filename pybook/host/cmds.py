import os


def set_environ(url):
    os.environ["PYBOOK_URL"] = str(url)
