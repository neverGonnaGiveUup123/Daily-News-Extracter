import requests, re, trafilatura, os
from bs4 import BeautifulSoup

r = requests.get("https://www.newshub.co.nz/home.html")


if str(r.status_code)[0] == "2":
    print("Site is available")

with open("src\\index.html", "w", encoding="utf-8") as fp:

    soup = BeautifulSoup(r.text, 'lxml')
    fp.write(str(soup))
    print(soup.attrs)
    eee = soup.find_all('a')
    counter = 0
    for i in eee:
        if re.search("c-NewsTile-imageLink", str(i)) != None:
            if re.search("href", str(i)) != None:
                listedElement = str(i).split(" ")
                linkText = listedElement[2].split('"')
                counter += 1
                downloaded = trafilatura.fetch_url(linkText[1])
                extractedText = trafilatura.extract(downloaded)
                with open(f"news\\ExtractedNewsStory{counter}.md", "w", encoding='utf-8') as file:
                    file.write(extractedText)