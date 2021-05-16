import io

import requests


def get(url: str):
  r = requests.get(url)
  return io.BytesIO(r.content)
