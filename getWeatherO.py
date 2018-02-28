#!/usr/local/bin/python3
"""
getWeatherO.py: Gets weather from OpenWeatherMap.org for the specified city,country code

Sample response:
{
'coord':
    {'lon': -73.75,
    'lat': 45.45},
'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}],
'base': 'stations',
'main': {'temp': 9.66, 'pressure': 994, 'humidity': 83, 'temp_min': 9, 'temp_max': 10},
'visibility': 24140,
'wind': {'speed': 11.8, 'deg': 240, 'gust': 16.5},
'clouds': {'all': 75}, 'dt': 1509400800,
'sys': {'type': 1, 'id': 3829, 'message': 0.166, 'country': 'CA', 'sunrise': 1509363193,
        'sunset': 1509399798},
'id': 5941925,
'name': 'Dorval',
'cod': 200
}
"""

import json, datetime, logging, requests
from getCityId import CityId

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def get_weather(querystring):
    """ This subroutine gets the current weather information """
    url = "https://api.openweathermap.org/data/2.5/weather"
    myweather = {}
    app_id = 'ed5b73b01e768e371f9a3dc6b2fbb452'

    req = url + querystring + '&units=metric' + '&APPID=' + app_id
    response = requests.get(req)

    myweather = json.loads(response.text)

    logging.debug(myweather)

    if myweather['cod'] == 200:
        print_weather(myweather)
    else:
        logging.error('Request error {:3d} returned from Server'.format(myweather['cod']))

    #print(myweather)

def get_forecast(querys, cnt=3):
    """ get_forecst: request the forecast endpoint that provides the weather forecast data """
    url = "https://api.openweathermap.org/data/2.5/forecast"
    myforecast = {}
    app_id = 'ed5b73b01e768e371f9a3dc6b2fbb452'

    req = url + querys + '&units=metric' + '&APPID=' + app_id + '&cnt=' + str(cnt)
    response = requests.get(req)

    myforecast = json.loads(response.text)

    logging.debug(myforecast)

    if myforecast['cod'] == '200':

        print("*"*95)

        for fsct in myforecast['list']:
            logging.debug(fsct)
            fd = datetime.datetime.fromtimestamp(fsct['dt']).strftime('%Y-%m-%d %H:%M')
            temp = float(fsct['main']['temp'])
            temp_min = float(fsct['main']['temp_min'])
            temp_max = float(fsct['main']['temp_max'])
            cond = fsct['weather'][0]['description']
            
            print('Forecast: {}:, Temp: {: 2.2f} C, Min: {: 2.2f} C, Max: {: 2.3f} C; Conditions: {}'.format(fd,
                                                                    temp, temp_min, temp_max, cond))
        print("*"*95)
        logging.error('Request error {:s} returned from Server'.format(myforecast['cod']))

def print_weather(wea, sel='current'):
    """ print_weather: prints the result from collecting the current weather info."""
    if sel == 'current':
        Title = "{} - {}".format(wea['name'], wea['sys']['country'])
        temperature = wea['main']['temp']
        temp_min = wea['main']['temp_min']
        temp_max = wea['main']['temp_max']
        humid = wea['main']['humidity']
        wind = wea['wind']['speed']
        wspd = float(wind)*3.6
        try:
            wind_gust = float(wea['wind']['gust']) * 3.6
        except KeyError:
            wind_gust = 0.0
        presIn = wea['main']['pressure']

        wd = int(wea['wind']['deg'])

        if wd == 0:
            wdt = "North"
        elif wd == 90:
            wdt = "East"
        elif wd == 180:
            wdt = "South"
        elif wd == 270:
            wdt = "West"
        elif wd > 0 and wd < 90:
            wdt = "North-East"
        elif wd > 90 and wd < 180:
            wdt = "South-East"
        elif wd > 180 and wd < 270:
            wdt = "South-West"
        else:
            wdt = "North-West"


        print("="*65)
        print("*\n*  Weather for {} provided by OpenWeatherMap.org".format(Title))
        print("*  Temperature is {}C with a min of {}C, and a max of {}C".format(temperature,
                                                                    temp_min, temp_max)) 
        print("*  Conditions: {} ".format(wea['weather'][0]['description']))
        if wind_gust != 0.0:
            print("*  Winds of {:2.2f} km/h, in direction {}, gusting at {:2.2f} km/h".format(wspd, 
                                                                    wdt, wind_gust))
        else:
            print("*  Winds of {:2.2f} km/h, in direction {}.".format(wspd, wdt))
        print("*  Humidity is {}%, with atmospheric pressure of {} hPa\n*".format(humid, presIn))
        print("="*65)
    elif type == 'forecast':
        logging.debug('Entering the Forecast section')
    else:
        logging.error("The type should be either current or forecast, we should not be here")



def main():
    """ This is the main routine. """
    #Select home or office weather
    try:
        #op = int(input("Please select (1) for HOME or (2) for OFFICE ?"))
        entry = input("Enter name of City, Contry code (ex. Montreal,CA): ")
    except ValueError:
        print("Please only use valid city names")
        raise SystemExit
    if entry == '':
        entry = 'Montreal,CA'
    city, cc = entry.split(',')

    cityId = CityId(city, cc)
    logging.debug(cityId.get_Id())
    querystring = '?id=' + str(cityId.get_Id())
    get_weather(querystring)
    get_forecast(querystring, cnt=6)



if __name__ == '__main__':
    main()
