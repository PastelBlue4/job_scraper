from requests import get
from bs4 import BeautifulSoup

from extractors.wwr import extract_wwr_jobs


result = extract_wwr_jobs("python")
print(result)
