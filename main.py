import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from keys import *
# proxy_client = TwilioHttpClient()
# proxy_client.session.proxies = {'https': os.environ['https_proxy']}


account_sid = 'ACd68140399aff3600f22d63702ebf89c6'

LAT = 33.781509
LON = -118.148979

parameters = {
    "appid": API_KEY,
    "lat": LAT,
    "lon": LON,
    "exclude": "current, minutely, daily"

}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:12]
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_='+15039804541',
        to='+17602211299'
    )

    print(message.status)