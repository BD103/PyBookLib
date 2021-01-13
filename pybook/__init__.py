import platform

from . import host  # noqa: F401
from .main import get, init  # noqa: F401

init()

if platform.system() == "Windows":
    from colorama import init as colorinit

    colorinit()
