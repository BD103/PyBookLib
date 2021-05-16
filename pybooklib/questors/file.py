import io


def get(path: str):
  with open(path, "rb") as fp:
    return io.BytesIO(fp.read())
