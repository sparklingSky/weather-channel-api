#!/usr/bin/python

__author__ = 'sparklingSky'

import urllib
from urllib import request
import json

# Replace [key] part of the URLs with your key.
ApiGeoLocationUrl = "http://api.wunderground.com/api/[key]/geolookup/q"
ApiForecastUrl = "http://api.wunderground.com/api/[key]/forecast"

# Examples of URLs:
#
# City, Country
# http://api.wunderground.com/api/[key]/geolookup/q/France/Paris.json
#
# Airport Code
# http://api.wunderground.com/api/[key]/geolookup/q/SFO.json

# Forecast
# http://api.wunderground.com/api/[key]/forecast/q/CA/San_Francisco.json
# or
# http://api.wunderground.com/api/[key]/forecast/q/zmw:00000.1.07157.json


def weatherForecast(location, locType):
    if locType == "c":
        location = location.split(" ")
        city = location[0]
        country = location[1]
        geoLocationUrl = ApiGeoLocationUrl + "/" + country + "/" + city + ".json"
    elif locType == "a":
        geoLocationUrl = ApiGeoLocationUrl + "/" + location + ".json"
    else:
        raise ValueError("Invalid Data")

    geoJSON = urllib.request.urlopen(geoLocationUrl)
    geoData = geoJSON.read()
    parsedGeo = json.loads(geoData.decode("utf-8"))
    geoJSON.close()

    unifiedLocation = parsedGeo["location"]["l"]

    weatherForecastUrl = ApiForecastUrl + unifiedLocation + ".json"

    weatherJSON = urllib.request.urlopen(weatherForecastUrl)
    weatherData = weatherJSON.read()
    parsedWeather = json.loads(weatherData.decode("utf-8"))
    weatherJSON.close()

    forecast = "Current weather: " + parsedWeather["forecast"]["txt_forecast"]["forecastday"][0]["fcttext_metric"] + \
               "\n" + parsedWeather["forecast"]["txt_forecast"]["forecastday"][1]["title"] + ": " \
               + parsedWeather["forecast"]["txt_forecast"]["forecastday"][1]["fcttext_metric"] + \
               "\n" + parsedWeather["forecast"]["txt_forecast"]["forecastday"][2]["title"] + ": " \
               + parsedWeather["forecast"]["txt_forecast"]["forecastday"][2]["fcttext_metric"] + \
               "\n" + parsedWeather["forecast"]["txt_forecast"]["forecastday"][3]["title"] + ": " \
               + parsedWeather["forecast"]["txt_forecast"]["forecastday"][3]["fcttext_metric"] + \
               "\n" + parsedWeather["forecast"]["txt_forecast"]["forecastday"][4]["title"] + ": " \
               + parsedWeather["forecast"]["txt_forecast"]["forecastday"][4]["fcttext_metric"] + \
               "\n" + parsedWeather["forecast"]["txt_forecast"]["forecastday"][5]["title"] + ": " \
               + parsedWeather["forecast"]["txt_forecast"]["forecastday"][5]["fcttext_metric"] + \
               "\n" + parsedWeather["forecast"]["txt_forecast"]["forecastday"][6]["title"] + ": " \
               + parsedWeather["forecast"]["txt_forecast"]["forecastday"][6]["fcttext_metric"] \
               + "\n" + parsedWeather["forecast"]["txt_forecast"]["forecastday"][7]["title"] + ": " \
               + parsedWeather["forecast"]["txt_forecast"]["forecastday"][7]["fcttext_metric"]

    return forecast

# Test 1
# print(weatherForecast("l'viv ukraine", "c"))

# Test 2
# print(weatherForecast("lwo", "a"))

# Test 4
# print(weatherForecast("", ""))
