import requests
from datatime import datetime
MY_LAT = -21.754530
MY_LONG = -41.324612
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position =(longitude, latitude)
#
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)

time_now = datetime.now()
print(time_now)