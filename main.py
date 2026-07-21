import os
import requests
from twilio.rest import Client

OWM_API_KEY = os.environ.get("OWM_API_KEY")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
MY_PHONE_NUMBER = os.environ.get("MY_PHONE_NUMBER")

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
LATITUDE = 19.431518
LONGITUDE = -98.905616

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": OWM_API_KEY,
    "cnt": 4,
}

will_rain = False

response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather = response.json()

for hour_data in weather["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        break

if will_rain:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="It's going to rain today. Remember to bring an umbrella ☔",
        to=MY_PHONE_NUMBER
    )
