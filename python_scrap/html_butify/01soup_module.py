from bs4 import BeautifulSoup

soup = BeautifulSoup(open("non_pritify.html"), "html.parser")

print(soup)  # read html file
print('*************************************')
print(soup.prettify())  # beautify html page

p = soup.prettify()

# write file
fi = open('pritify.html', 'w')
fi.write(p)
fi.close()
