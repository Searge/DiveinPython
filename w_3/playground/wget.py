import sys
import requests
# from pprint import pprint

url = sys.argv[1]
try:
    response = requests.get(url, timeout=30)
except requests.Timeout:
    print(url, '— Надто довго завантажується.')
else:
    print(response.content)
