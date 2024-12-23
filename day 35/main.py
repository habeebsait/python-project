import requests

from twilio.rest import Client
auth_token = "07119c83ac9ae32fe7999772e0bf985c"



number = +12565790313



api_key = "eab5cc8397539e1518171b018ca3077a"

OWN_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

LAT = 13.012182
LON = 77.593154

parameters = {
    "lat" : LAT,
    "lon" : LON,
    "appid" : api_key,
    "cnt" : 4
}


response = requests.get(OWN_endpoint, params= parameters)
response.raise_for_status()

weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    weather_id = hour_data["weather"][0]["id"]
    if weather_id <700:
        will_rain = True

if will_rain:
    client = Client(auth_token)

    message = client.messages.create(
    to="+91 6366699999",
    from_  = number,
    body = "It will rain today ☔️",
)
print(message.status)

