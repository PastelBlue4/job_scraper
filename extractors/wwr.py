from requests import get
from bs4 import BeautifulSoup


def extract_wwr_jobs(keyword):

    main_url = "https://weworkremotely.com/remote-jobs/search?term="

    response = get(f"{main_url}{keyword}")
    if response.status_code != 200:
        print("정보 받아오기 실패")
    else:
        soup = BeautifulSoup(response.text, "html.parser")

        jobs = soup.find_all("section", class_="jobs")
        print(len(jobs))
