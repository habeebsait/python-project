from bs4 import BeautifulSoup
import requests

response = requests.get(url = "https://news.ycombinator.com")
website = response.text

soup = BeautifulSoup(website, "html.parser")

print(soup.title)

namesid =[]
scoresid = []
names =[]
scores = []


name = (soup.findAll(name = "tr", class_ ="athing submission"))
for i in name:
    namesid.append(i.get("id"))
    names.append(i.getText())

score = soup.findAll(name = "span", class_ = "score")

for i in score:
    scoresid.append(i.get("id")[6:])
    scores.append(i.getText())

j =0

for i in range(len(names)):
    if namesid[i] == scoresid[j]:
        

        print(names[i])
        print(scores[j])
        j+=1

    else:

        pass
