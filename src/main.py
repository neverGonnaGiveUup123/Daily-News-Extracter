import requests, re, trafilatura
# import requests to fetch website, regex to find attributes and trafilatura for clean text scraping
from bs4 import BeautifulSoup
#import beautifulSoup to parse html

r = requests.get("https://www.newshub.co.nz/home.html")
#get website

if str(r.status_code)[0] == "2":
    #execute this code if client successfully connects to the website, else quit
    with open("src\\index.html", "w", encoding="utf-8") as fp:
        # open a new index.html in src folder
        soup = BeautifulSoup(r.text, 'lxml')
        # get the html of the website
        fp.write(str(soup))
        # copy the same html into index.html
        foundElements = soup.find_all('a')
        # find all <a> elements
        counter = 0
        # create counter to number extracted news stories
        for i in foundElements:
            # for every <a> element found in index.html
            if re.search("c-NewsTile-imageLink", str(i)) != None:
                # if regex finds "c-NewsTile-imageLink" as an attribute inside an <a> element
                if re.search("href", str(i)) != None:
                    # if regex also finds "href" as an attribute
                    listedElement = str(i).split(" ")
                    # create a list of all the attributes in the <a> with each attr as an item
                    linkText = listedElement[2].split('"')
                    # create another list with the "href" attr and isolate the url
                    counter += 1
                    # this is for numbering each story
                    downloaded = trafilatura.fetch_url(linkText[1])
                    # use the isolated link and connect to the news page it leads to
                    extractedText = trafilatura.extract(downloaded)
                    # extract all the text from the page
                    # Trafilatura removes noise
                    with open(f"news\\ExtractedNewsStory{counter}.md", "w", encoding='utf-8') as file:
                        file.write(extractedText)
                        # create a new markdown file and write the extracted text to that file
else:
    # if status code 300, 400, 500 then quit (redirect, client error, server error)
    quit("Site is down")
