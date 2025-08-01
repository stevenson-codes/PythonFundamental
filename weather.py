import requests

city = 'Vancouver'
url = f'http://api.weatherapi.com/v1/current.json?key=df2dbb22e84c4783b8b32242250108&q={city}&aqi=no'
response = requests.get(url)
weather_json = response.json()

temp = weather_json['current']['temp_c']
description = weather_json['current']['condition']['text']

print(f"Today's weather in {city} is {description.lower()} and {temp} degrees")