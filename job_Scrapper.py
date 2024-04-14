import requests
from bs4 import BeautifulSoup
import time

skill_set = input("Provide your skill set in comma separated format : ")
skill_set = skill_set.split(",")

def scrap_jobs():
    # Fetch the html content of webpages : requests
    html_texts = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=").text
    #print(html_texts)

    # scrap the data to fetch the results : BeautifulSoup
    soup = BeautifulSoup(html_texts, 'lxml')
    #print(soup.prettify())

    #company_name = soup.find("h3", class_="joblist-comp-name").text.replace(" ", "").strip()
    #print(company_name)

    #skills = soup.find("span", class_="srp-skills").text.replace(" ", "").strip().split(",")
    #print(skills)

    #date_posted = soup.find("span", class_="sim-posted").text.strip()

    # print(f'''
    # Company Name : {company_name}
    # Skills Needed : {skills}
    # Date Published : {date_posted}
    #       ''')

    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    for job in jobs:
        date_posted = job.find("span", class_="sim-posted").text.strip()
        skills = job.find("span", class_="srp-skills").text.replace(" ", "").strip().split(",")
        if "few" in date_posted and set(skill_set) & set(skills):
            company_name = job.find("h3", class_="joblist-comp-name").text.replace(" ", "").strip()
            jd = job.header.h2.a['href']

            print(f'''
        Company Name : {company_name}
        Skills Needed : {skills}
        JD : {jd}
        ''')
            print("##############")

if __name__ == "__main__":
    while True:
        scrap_jobs()
        print("waiting for 5 secs")
        time.sleep(5)
    