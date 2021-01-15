import os


def make_lib():
    if ".library" not in os.listdir():
        os.mkdir(".library")


def make_user(user):
    make_lib()
    fmt_user = user.replace(" ", "-")
    if fmt_user not in os.listdir(".library"):
        os.chdir(".library")
        os.mkdir(fmt_user)
        os.chdir("../")


def pylib_init(sample=False):
    make_lib()
    if sample:
        make_user("BD103")
