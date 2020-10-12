#!/usr/bin/python3
from urllib.request import Request, urlopen
from datetime import date
from lxml import html
from os import getcwd

file_date = str(date.today())
today = date.today().strftime("%Y/%m/%d")
sans_today = date.today().strftime("%Y-%m-%d")
path = getcwd()
sources_today = []

# TODO Expand to grab more sources and then create daily job to run and gather nightly
# TODO Going to have to figure a way to grab not soley based off date in link


def getMicrosoft(url):
    # Grab Microsoft security blog page html, without headers set
    # blog will reject your request
    page = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = html.fromstring(urlopen(page).read())

    # Loop through links on page and add to sources_today if posted 
    # on the current date and not in list
    for link in webpage.xpath("//a"):
        if (today in str(link.get("href"))) \
        and (str(link.get("href")) not in sources_today):
            sources_today.append(str(link.get("href")))
    return sources_today


def getSans(url):
    page = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = html.fromstring(urlopen(page).read())

    for link in webpage.xpath("//a"):
        if (sans_today in str(link.get("href"))) \
        and (str(link.get("href")) not in sources_today):
            sources_today.append('https://isc.sans.edu/' + str(link.get("href")))
    return sources_today


# If at least one link was pulled, print to a file with current date
# * Replace f"{path}/..." with your preferred directory and naming 
# TODO add functionality to post to website as a blog daily
# TODO add functionality to auto break out under a org header
def aggregation(sources_today):
    if len(sources_today) != 0:
        with open(f"{path}/{file_date}_sources.txt", "w") as f:
            for x in sources_today:
                f.write(x + "\n")
