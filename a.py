from tkinter import *
import requests
import json
import datetime

api_key = "6ee92ba32fe4dec80b3385870289980e"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Введите название города : ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":

    y = x["main"]

    current_temperature = y["temp"]

    current_pressure = y["pressure"]

    current_humidity = y["humidity"]

    z = x["weather"]

    weather_description = z[0]["description"]

    print(" Температура (в единицах Кельвина) = " +
          str(current_temperature) +
          "\n атмосферное давление (в единицах ГПа) = " +
          str(current_pressure) +
          "\n влажность (в процентах) = " +
          str(current_humidity) +
          "\n описание = " +
          str(weather_description))

else:
    print(" Город не найден ")