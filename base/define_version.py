import requests
import os

stage = os.getenv('STAGE', 'test')
pkg_name = os.environ['PKG_NAME']
dir_name = os.environ['DIR_NAME']
host = 'pypi.org' if stage == 'prod' else 'test.pypi.org'
try:
    json = requests.get(f'https://{host}/pypi/{pkg_name}/json').json()
    version = json['info']['version']
except Exception:  # first deploy
    version = '0.0.0'
x100, x10, x = map(int, version.split('.'))
new_version = ".".join(str(x100 * 100 + x10 * 10 + x + 1).zfill(3))
paths = [
    f"/app/{dir_name}/__version__.py",
    f"/app/__version__.py",
]
for path in paths:
    with open(path, "w") as f:
        f.write(f"__version__ = '{new_version}'")
print(stage, f"__version__ = '{new_version}'")
