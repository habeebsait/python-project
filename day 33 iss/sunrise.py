import requests 

response = requests.get(url = "https://api.sunrise-sunset.org/json")
print(response.json)