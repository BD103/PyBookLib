import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pybooklib",
    version="1.0",
    author="BD103",
    author_email="dont@stalk.me",
    description="Create, upload, and use Python project templates.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BD103/PyBookLib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "click",
        "requests",
        "flask",
        "getch",
        "importlib_resources ; python_version<'3.7'",
        # "colorama ; platform_system=='Windows'",
    ],
    entry_points={"console_scripts": ["pybook=pybook.cli:cli", "pylib=pylib.cli:cli"]},
    include_package_data=True,
    python_requires=">=3.8",
)
