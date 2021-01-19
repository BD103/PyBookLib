import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pybooklib",
    version="1.1",
    author="BD103",
    author_email="dont@stalk.me",
    description="Create, upload, and use Python project templates.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BD103/PyBookLib",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={"": ["data/*.md", "pylib/data/*.html"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Framework :: Flake8",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Communications :: File Sharing",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Software Development",
    ],
    install_requires=[
        "click",
        "requests",
        "flask",
        "rich",
        "importlib_resources ; python_version<'3.7'",
        # "colorama ; platform_system=='Windows'",
    ],
    entry_points={
        "console_scripts": [
            "pybooklib=pybooklib.pybooklib_cli:about",
            "pybook=pybooklib.pybook_cli:cli",
            "pylib=pybooklib.pylib_cli:cli",
        ]
    },
    python_requires=">=3.8",
)
