import json
import os

from flask import Flask, request, send_file

from . import data

try:
    import importlib.resources as pkg_resources
except ImportError:
    # For Python < 3.7
    import importlib_resources as pkg_resources

app = Flask("app")


@app.route("/")
def index():
    return pkg_resources.read_text(data, "index.html")


@app.route("/api", methods=["GET", "POST"])
def api():
    user = request.args.get("u")
    book = request.args.get("b")
    version = request.args.get("v")

    try:
        fmt_version = version.replace(".", "-")
    except AttributeError:
        fmt_version = None

    if user is None:
        return {"type": "UserError", "content": "User is not specified in request."}
    elif user not in os.listdir(".library/"):
        return {"type": "UserError", "content": "User is not registered in library."}
    elif book is None:
        return {"type": "User", "content": os.listdir(f".library/{user}")}
    elif book not in os.listdir(f".library/{user}"):
        return {"type": "BookError", "content": "Book is not registered under user."}
    elif os.listdir(f".library/{user}/{book}") == []:
        return {"type": "BookError", "content": "Book's contents do not exist."}
    elif version is None:
        latest = os.listdir(f".library/{user}/{book}")[-1]
        return send_file(f".library/{user}/{book}/{latest}")
    elif fmt_version + ".zip" not in os.listdir(f".library/{user}/{book}"):
        return {"type": "VersionError", "content": "Version specified does not exist."}
    else:
        return send_file(f".library/{user}/{book}/{fmt_version}.zip")


def run(host="0.0.0.0", port=8000):
    app.run(host=host, port=port)
