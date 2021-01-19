# About PyBookLib

PyBookLib is a two part library designed to host and get template code projects. It is written for mainly Python programs, but it is possible to host other languages as well. PyBookLib has two submodules, each independant of one another: PyBook and PyLib. PyBookLib has no affiliations with the existing PyPI projects [PyBook](https://pypi.org/project/pybook) and [PyLib](https://pypi.org/project/pylib). It is a completely separated project, and just happened to be library themed. 😁

## Install

You can install the package through the following:

```console
> pip install -U pybooklib
```

If you want the latest development version, which most definitely has bugs, run the following:

```console
> pip install git+https://github.com/BD103/PyBookLib
```

## Use

To pull up this screen in the console, you can run `pybooklib` in the command line. Running `pybook` or `pylib` gives a list of possible commands with each.

### PyBookLib

The main PyBookLib module has no current function beyond a code bridge and displaying this markdown file in the command line.

```console
> pybooklib
```

### PyBook

PyBook's main functionality is connecting to a hosted library and receiving _books_ (`.zip` files). The library that is accessed is defined by an environmental variable. Try running something like this:

```python
from pybooklib import pybook
import os

# Set environmental variable for library. Unecessary but helpful all the same
pybook.set_url("https://library.bd103.repl.co/api")

# Gets a book "sample-library" from the user "BD103" with the version "1.2" and extracts contents to the directory "pylib-library"
pybook.get(user="BD103", book="sample-library", version="1.2", direc="pylib-library")
```

With this simple script, it connects to [library.bd103.repl.co](https://library.bd103.repl.co) and requests sample-library. This book is a sample script to host your own library. (It was created for [Replit](https://repl.it), so that's why there is a pyproject.toml.)

You can also run some bash commands:

```console
# Get a list of commands
> pybook --help
> pybook get-book BD103 sample-library --version 1.2 --direc pylib-library
> pybook get-user BD103
# This should automatically be set to library.bd103.repl.co/api
> pybook set-url https://link.to.site/api
# Umbrella get function to specify exact details
> pybook get --user BD103 --direc folder
```
You do not have to specify all these parameters. Try removing and replacing some of them and see what happens!

### PyLib

PyLib is for hosting your own library. It is extremely simple. Install pybooklib, and choose your path:

> Note: These paths will automatically set the IP and Port to `0.0.0.0:8000`. If on a local machine, you can connect through [localhost:8000](https://localhost:800). If using a server hosting service, it should automatically set the host to your domain. If you are having conflicts with the port, or want a different IP, you can specify it by taking the Python main.py path and replacing `pylib.run()` with `pylib.run(host="1.2.3.4", port=8080)`.

#### Python main.py

Create a file called main.py. Inside, paste the following:

```python
from pybooklib import pylib

pylib.run()
```

Run the script to start hosting your library.

#### CLI

In the command line, run the following:

```console
pylib run
```

Watch as your server gets hosted.

## Contributing

If you want to contribute to this project, go to [github.com/BD103/PyBookLib](https://github.com/BD103/PyBookLib), create a fork and a pull request. All code should be run through the following commands:

```
black pybooklib
isort pybooklib --profile black
flake8 pybooklib
```

PyTest is not yet implemented. Stay tuned! 🎵
