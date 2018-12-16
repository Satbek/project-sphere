import json
import geopy.distance as distance
import pandas as pd
import requests

def get_near_metro(lon, lat, api_key):
    req_text = 'https://search-maps.yandex.ru/v1/?text=метро&ll=' + str(lon) + "," + str(lat) + '&lang=ru_RU&results=1&apikey=' + api_key
    ans = json.loads(requests.get(req_text).text)
    try:
        metro_lon, metro_lat = ans['features'][0]['geometry']['coordinates']
        result = distance.vincenty((lon, lat), (metro_lon, metro_lat)).m
    except:
        result = np.nan
    return result
