import requests
import os
from twilio.rest import Client

longitude = 120.412521
latitude = 53.810331

# Twilio web service.
account_sid = 'my_account_sid_number_in_twilio_account.'
auth_token = 'auth_token_in_twilio_account.'

# This is API section.
app_id = "Api_id_in_online."
url = "Weather_api_url."

#  Call the key for request.get() class.
make_dict = {
    'q': "Name_of_place.",
    'appid': app_id,
    'exclud': "minutely,daily,monthly"
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
        from_="Phone_number_here_in_twilio_api_webservice.",
        to="To_whom_to_send_the_number."
    )
    print("massage deliverd")