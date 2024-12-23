import requests
from datetime import *
MY_LAT = 12.986051
MY_LNG = 77.589445


response = requests.get(url = "http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "tzid": "Asia/Kolkata",
    "formatted": 0,
}

response1 = requests.get("https://api.sunrise-sunset.org/json", params = parameters)

data = response1.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)


time_now = datetime.now()
print(time_now.hour)

print(time_now)

