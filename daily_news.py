#/usr/bin/python3

# Created by Spencer Mertes
# https://twitter.com/MertleTrtl3
# 5/1/2020

from siteSources.grab_source import *

getMicrosoft("https://www.microsoft.com/security/blog/")
getSans('https://isc.sans.edu/diaryarchive.html')

aggregation(sources_today)
