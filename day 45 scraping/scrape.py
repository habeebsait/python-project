from bs4 import BeautifulSoup

with open("web scrapping/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.prettify())

# h3_heading = soup.find(name= "h3")
# print(h3_heading)

url = soup.select_one(selector="p a")
print(url)
