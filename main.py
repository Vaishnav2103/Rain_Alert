import requests
from twilio.rest import Client
api_key = "9902dbeef07288d64fb27c4ec5ea586c"
parameter = {
    "lat": "23.810331",
    "lon": "90.412521",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
account_sid = "ACa29790dd4a7958e3c03bacc3c181d1e8"
auth_token = "c8a867251a75ec5419d47cb98a4ffc91"

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameter)
print(response.status_code)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain = False
for hour in weather_slice:
    rain_alert = hour["weather"][0]["id"]
    if rain_alert < 700:
        will_rain = True

if will_rain is True:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It is going to rain, Bring an Umbrella Today",
            from_="+18509003252",
            to="+918130804845"
        )

    print(message.status)

# Hey love! Two Weeks ago I saw you at Manhattan (Took some time to get you Number 😉), and I am completely in love with you i would really like it if we could go on a date sometimes? I will make sure you will not regret.Love Harry
