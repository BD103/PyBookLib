import io

import requests


def _get_url(id: str, package_type="sdist"):
  r = requests.get(f"https://pypi.org/pypi/{id}/json")

  urls = r.json()["urls"]
  url = None

  for i in urls:
    if i["packagetype"] == package_type:
      url = i["url"]
      break

  return url


def get(id: str):
  url = _get_url(id)

  if url is None:
    return None
  else:
    r = requests.get(url)
    return io.BytesIO(r.content)
