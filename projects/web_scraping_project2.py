from bs4 import BeautifulSoup
import requests
print("put som unfamiliar skill")
unfamiliar_skill=input(">")
print(f"filtering out {unfamiliar_skill}")
html_text=requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
soup=BeautifulSoup(html_text, "lxml")
jobs=soup.find_all("li",class_="clearfix job-bx wht-shd-bx")
for job in jobs:
    job_puplished_date=job.find("span", class_="sim-posted").text
    if "few" in job_puplished_date:
        company_name=job.find("h3",class_="joblist-comp-name").text.replace(" ","")
        skill_requirments=job.find("span", class_="srp-skills").text.replace(" ","")
        more_info=job.header.h2.a["href"]
        if unfamiliar_skill not in skill_requirments:
            print(f"company name:{company_name.strip()}")
            print(f"skills required:{skill_requirments.strip()}")
            print(f"job puplished:{job_puplished_date.strip()}")
            print(f"job link:{more_info}")
            print(" ")