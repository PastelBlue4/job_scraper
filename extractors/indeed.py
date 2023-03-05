from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


browser = webdriver.Chrome()

browser.get("https://kr.indeed.com/jobs?q=python")

soup = BeautifulSoup(browser.page_source, "html.parser")


job_list = soup.find("ul", class_="jobsearch-ResultsList")


jobs = job_list.find_all("li", recursive=False)


for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None:
        print("job li")
    else:
        print("mosac li")


while True:
    pass
