# https://www.reddit.com/ data
from urllib.request import urlopen

from bs4 import BeautifulSoup

site_url = urlopen("http://www.reddit.com")
data = site_url.read()
#print(data)
site_url.close()

soup = BeautifulSoup(data, "html.parser")
print(soup.prettify())
