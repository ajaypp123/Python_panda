# html - html.parser
# xml - lxml.parser

# find title of web page

from bs4 import BeautifulSoup

soup = BeautifulSoup(open("moive.html"), "html.parser")

# find title of web page saparated by space
title = soup.html.head.title.get_text(' ')
print("************************************************")
print(title)
print("************************************************")

