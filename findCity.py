#!/Users/josefernandez/anaconda3/bin/python
import csv
""" This class searches the file GeoLiteCity-Location.csv file
and takes the first match of the city to then get the latitude and longitude
values """


class findCity:
    def __init__(self, city):
        self.city = city
        self.lat = ''
        self.lng = ''

        with open('./GeoLiteCity-Location.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                lc = row[3].upper()
                if lc == self.city.upper():
                    self.lat = row[5]
                    self.lng = row[6]
                    print("Found City {}, lat: {}, Long: {}".format(
                        lc, self.lat, self.lng))
                    break
        f.close()

    def get_lat(self):
        return self.lat

    def get_lng(self):
        return self.lng
