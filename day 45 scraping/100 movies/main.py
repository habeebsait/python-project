import requests
from bs4 import BeautifulSoup

response = requests.get(url = "https://www.timeout.com/film/the-100-best-bollywood-movies-the-list")

website = (response.text)

soup = BeautifulSoup(website, "html.parser")

data = soup.findAll(name = "h3", class_ = "_h3_70r6w_1")

num = 100
j = 1

# with open("day 45/100 movies/movies.txt", "a") as file:

    # for i in data:
    #     file.write(str(j)+ ". ")
    #     if num == 100:
    #         file.write(i.getText()[5:])
    #     elif num <100 and num > 9:
    #         file.write(i.getText()[4:])
    #     else:
    #         file.write(i.getText()[3:])

    #     file.write("\n")
    #     num -=1
    #     j+=1


# OR **************
 
with open("day 45 scraping/100 movies/movies.txt", "a") as file:
    for i in range(len(data)-1, -1, -1):
        file.write(data[i].getText())
        file.write("\n")
