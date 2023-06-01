import requests
import os
from twilio.rest import Client

longitude = 120.412521
latitude = 53.810331

account_sid = 'AC970466a3e4666ce524b8a1287bc3249a'
auth_token = 'ed892104d55db8d6ca599867767041f4'

app_id = "6e0673bebee743b58f295b71275f13a3"
url = "https://api.openweathermap.org/data/2.5/weather?"


make_dict = {
    # 'lat': 23.810331,
    # 'lon': 90.412521,
    'q': "Dinajpur, Dhaka,bangladesh",
    'appid': app_id,
    'exclud': "minutely,daily"
}


response = requests.get(url=url, params=make_dict)
response.raise_for_status()

data = response.json()

print(data)
only_weather = data['weather'][0]['id']

will_rain = False

if int(only_weather) < 700:
    will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Hi, this is test message for twilio api.",
        from_="+13203825930",
        to="+8801739933258"
    )
    print("massage deliverd")