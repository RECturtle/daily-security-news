#!usr/bin/python3

from urllib.request import Request, urlopen
from datetime import date
from lxml import html

file_date = str(date.today())
today = date.today().strftime("%Y/%m/%d")
sources_today = []

# TODO Expand to grab more sources and then create daily job to run and gather nightly

def getMicrosoft(url):
    page = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = html.fromstring(urlopen(page).read())

    for link in webpage.xpath("//a"):
        if today in str(link.get("href")) and str(link.get("href")) not in sources_today:
            sources_today.append(str(link.get("href")))

    if len(sources_today) != 0:
        with open("/home/mertle/news/" + file_date + "_sources.txt", "w") as f:
            for x in sources_today:
                f.write(x + "\n")
