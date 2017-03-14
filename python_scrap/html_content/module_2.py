from bs4 import BeautifulSoup

soup = BeautifulSoup(open("moive.html"), "html.parser")

#######################################################
# soup.html.body - all data under body start with body tag
# soup.html.body.contents[1] - all contents under body start with div tag
# soup.html.body.next - move next
# soup.html.body.name - tag name under body
# soup.html.body.get_text(' ') - all text data under body
# soup.html.body.string - single text line

# soup.html.body.find_all('div')    soup.find_all(text="Genre:")

# soup.html.body.div.nextSibling - next div under body
# <body> <div></div> <div>a</div> ====> a soup.html.body.div.nextSibling
####################################################


# content under body
data = soup.html.body.contents[1]
#print(data)

# use next to skip current tag
# print(soup.html.body.next.next.next.next.get_text(' '))
# print(soup.html.body.name)                 # get tag name

# movie Genre
print(soup.find_all(id="meta"))
