import os


def init():
    if ".library" not in os.listdir():
        os.mkdir(".library")
