#!/usr/bin/env python3
# Get the City ID from Json file downloaded from OpenWeatherMap.org "city.lost.json"

import json
import logging
import requests

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class CityId:
    def __init__(self, name, county_code, source):
        self.cityname = name
        self.cc = county_code
        self.source = source
        self.cityInfo = {
            "id": 0,
            "name": "",
            "country": "",
            "coord": {
                "lon": 0,
                "lat": 0
            }
        }

        if self.source == "API":
            headers = {
                # "RapidAPIProject": "weather-app",
                "X-RapidAPI-Key": "v1UW8gDjyYmshYh5MCIJ5VHTAlwwp1Jur8OjsnZUacOtDRz6y7"
            }

            response = requests.get(
                "https://devru-latitude-longitude-find-v1.p.rapidapi.com/latlon.php?location="+name+"%2C"+county_code, headers=headers)

            if ((response.status_code == 200) & (int(response.headers['Content-Length']) > 33)):
                logging.debug(response.headers)
                s = json.loads(response.content)
                logging.debug(s['Results'][0]['lat'])
                self.cityInfo['name'] = s['Results'][0]['name']
                self.cityInfo['country'] = s['Results'][0]['c']
                self.cityInfo['coord']['lon'] = s['Results'][0]['lon']
                self.cityInfo['coord']['lat'] = s['Results'][0]['lat']
            else:
                logging.error(
                    "City was not Found - status {}".format(response.status_code))
                raise SystemExit
        else:
            with open('city.list.json', "rb") as f:
                text = f.read()
                data = json.loads(text)
                for record in data:
                    if (record['name'] == self.cityname) and (record['country'] == self.cc):
                        logging.debug(record)
                        self.cityInfo = record
                        found = True
                        break
                    else:
                        found = False
            f.close()
            if not found:
                logging.error("City was not Found")
                raise SystemExit

    def __str__(self):
        return 'ID for {} is: {}'.format(self.cityname, self.cityInfo["id"])

    def get_Id(self):
        return self.cityInfo['id']

    def get_Coord(self):
        return self.cityInfo['coord']
