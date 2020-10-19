import subprocess
import sys
from __version__ import __version__
import time
import os

pkg_name = os.environ['PKG_NAME']
stage = "prod" if sys.argv[1] == "prod" else 'stg'
chunks = [sys.executable, "-m", "pip",
          "install", f'{pkg_name}=={__version__}']
if stage == "stg":
    chunks.insert(4, "https://test.pypi.org/simple/")
    chunks.insert(4, "--index-url")

print(*chunks)

for i in range(100):
    try:
        subprocess.check_call(chunks)
    except Exception as e:
        print(e)
        time.sleep(10)
    else:
        break
