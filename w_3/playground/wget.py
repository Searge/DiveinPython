import sys
import requests
# from pprint import pprint

url = sys.argv[1]
try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
except requests.Timeout:
    print(url, '— Надто довго завантажується.')
except requests.HTTPError as err:
    code = err.response.status_code
    print(f"Сайт {url} видав код: {code}")
except requests.RequestException:
    print('Помилка скачування', url)
else:
    print(response.content)
