from requests import get

from bs4 import BeautifulSoup


base_url = "https://search.shopping.naver.com/search/all?query=%EA%B0%84%EC%9E%A5%EA%B2%8C%EC%9E%A5"


response = get(f"{base_url}")

if response.status_code != 200:
    print(response.text)
else:
    print(response.text)
