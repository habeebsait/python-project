import requests
import smtplib
from datetime import datetime
import time

MY_LAT =  13.049011 # Your latitude
MY_LONG = 77.546544 # Your longitude
my_email = "habeebsait04@gmail.com"
password = "****"

def near_me(lat,lng):
    global MY_LAT, MY_LONG
    lat_near = False
    lng_near = False
    if lat - MY_LAT > -5 and lat - MY_LAT <5 and lng - MY_LONG > -5 and lng - MY_LONG <5:
        return True
    else:
        return False
    

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

print(iss_latitude)
print(iss_longitude)

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "tzid": "Asia/Kolkata",
    "formatted": 0,
}

def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    print(f"sunrise: {sunrise}")
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(f"sunset: {sunset}")

    time_now = datetime.now()
    hour_now = time_now.hour
    print(f"Hour now: {hour_now}")
    if 23 > hour_now > sunset or hour_now < sunrise:
        return True
    else:
        return False

near_me_sat = near_me(iss_latitude, iss_longitude)
print(near_me_sat)

print(is_night())


keep_running = True
while True:
    if near_me_sat and is_night:
        print("The ISS Satelite is near me! and it is dark")

    #If the ISS is close to my current position

    # and it is currently dark

    # Then send me an email to tell me to look up
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:ISS SATELITE\n\nLook up the satelite is above u Time: {datetime.now()}")
        connection.close()
    print("ok")
    time.sleep(60)



# BONUS: run the code every 60 seconds.



