import datetime as dt
import requests

baseurl="http://api.openweathermap.org/data/2.5/weather?"

api_key="ed54f9d7486d2edeb84114f5c8b922f4"

city=input('Enter City: ')

def kel_to_cel_fahren(kelvin):
    celsius=kelvin-273
    fahrenheit=celsius*(9/5)+32
    return celsius,fahrenheit

url= baseurl + 'appid=' + api_key + '&q=' + city
response=requests.get(url).json()
# print(response)

temp_kelvin=response['main']['temp']
temp_celsius, temp_fahrenheit=kel_to_cel_fahren(temp_kelvin)
max_temp=response['main']['temp_max']
tempc,tempf=kel_to_cel_fahren(max_temp)
min_temp=response['main']['temp_min']
temc,temf=kel_to_cel_fahren(min_temp)
humidity=response['main']['humidity']
description=response['weather'][0]['description']
sunrise=dt.datetime.utcfromtimestamp(response['sys']['sunrise']+response['timezone'])
sunset=dt.datetime.utcfromtimestamp(response['sys']['sunset']+response['timezone'])

print(f"Tempertature in {city}: {temp_celsius:.2f}'C or {temp_fahrenheit}'F")
print(f"Maximum Tempertature in {city}: {tempc:.2f}'C or {tempf}'F")
print(f"Minimum Tempertature in {city}: {temc:.2f}'C or {temf}'F")
print(f"Humidity in {city}: {humidity}%")
print(f"General Weather in {city}: {description}")
print(f"Sunrises in {city} at {sunrise}.")
print(f"Sunsets in {city} at {sunset}.")