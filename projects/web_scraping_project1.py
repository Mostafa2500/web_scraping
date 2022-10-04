from bs4 import BeautifulSoup as bs
import requests
import csv
request=requests.get("https://coreyms.com/").text
soup= bs(request, "lxml")
articls= soup.find_all("article")
with open("coreyms_website_2.csv","w") as f:
    thewriter=csv.writer(f)
    header=["header","summary","youtube link"]
    thewriter.writerow(header)
    for article in articls:

        header= article.find("h2", class_="entry-title").a.text.replace("\n","")
        summary=article.find("div", class_="entry-content").p.text.replace("\n","")
        try:

            link=article.find("iframe", class_="youtube-player")["src"]
            vid_id= link.split("/")[4]
            vid_id=vid_id.split("?")[0]
            youtube_link= f"https://youtube.com/watch?v={vid_id}"
        except:
            print(None)
        info=[header,summary,youtube_link]
        thewriter.writerow(info)
        
    # print(f"{header}\n")
    # print(f"{summary}\n")
    # print(f"{youtube_link}\n")
    # print()
    # print()