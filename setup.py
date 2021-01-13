import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pybook",
    version="1.0",
    author="BD103",
    author_email="dont@stalk.me",
    description="Create, upload, and use Python project templates.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BD103/PyBook",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "click",
        "requests",
        "colorama ; platform_system=='Windows'",
        "importlib_resources ; python_version<'3.7'",
    ],
    extras_require={"host": ["flask"]},
    entry_points={"console_scripts": ["pybook=pybook.cli:cli"]},
    python_requires=">=3.8",
)
