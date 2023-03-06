from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def extract_ind_jobs(keyword):

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )
    browser.get(f"https://kr.indeed.com/jobs?q={keyword}")
    soup = BeautifulSoup(browser.page_source, "html.parser")

    results = []

    job_list = soup.find("ul", class_="jobsearch-ResultsList")
    jobs = job_list.find_all("li", recursive=False)

    for job in jobs:
        zone = job.find("div", class_="mosaic-zone")
        if zone == None:
            anchor = job.select_one("h2 a")

            title = anchor.find("span").string
            link = anchor["href"]
            preview_container = job.find("div", class_="result-footer")

            create_at = preview_container.find("span", class_="date")
            create_at.span.extract()
            extract_create_at = create_at.string

            preview = preview_container.select_one("div").string
            if preview == None:
                preview = "미리보기 정보가 없어요."

            info_container = job.find("div", class_="company_location")
            company_name = info_container.select_one("span").string
            company_location = info_container.select_one("div").string

            job_data = {
                "company_name": company_name.replace(",", " "),
                "location": company_location.replace(",", " "),
                "detail_info": preview.replace(",", " "),
                "create_at": extract_create_at.replace(",", " "),
                "link": f"https://kr.indeed.com{link}".replace(",", " "),
            }
            results.append(job_data)

    return results
