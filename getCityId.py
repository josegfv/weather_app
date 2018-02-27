#! Python 3
# Get the City ID from Json file downloaded from OpenWeatherMap.org "city.lost.json"

import json, logging

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class CityId:
    def __init__(self, name, county_code):
        self.cityname = name
        self.cc = county_code
        self.cityInfo =  {}

        with open('city.list.json' , "rb") as f:
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
