from flask import Flask
try:
    import importlib.resources as pkg_resources
except ImportError:
    # For Python < 3.7
    import importlib_resources as pkg_resources
from . import data

app = Flask("app")


@app.route("/")
def index():
    return pkg_resources.read_text(data, "index.html")


def run(host="0.0.0.0", port=8000):
    app.run(host=host, port=port)
