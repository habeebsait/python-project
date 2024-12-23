import requests
from datetime import datetime

TOKEN = "bhdcsaknxdasdc"
username = "habeebsait"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username" : username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url= pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "ajisai"
}

headers  = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url = graph_endpoint, json= graph_config, headers= headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{username}/graphs/graph1"

today = datetime.now()

date = today.strftime("%Y%m%d")

pixel_data ={
    "date": date,
    "quantity" : "310.1",
}

# response = requests.post(url = pixel_creation_endpoint, json = pixel_data, headers= headers)
# print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{username}/graphs/graph1/20241022"

pixel_update = {
    "quantity" : "4.7"
}

response = requests.put(url = pixel_update_endpoint, json = pixel_update, headers=headers)
print(response.text)



 



