import requests
import json
from findCity import findCity as fc

def getWeather(querystring):

    url = "https://simple-weather.p.mashape.com/weatherdata"
    myweather = {}

    headers = {
        'x-mashape-key': "YyECNDs53smsh3hRwtAAhvl4LJq2p1mAuosjsnCg3rsDvDSiY5",
        'accept': "application/json",
        'cache-control': "no-cache",
        'postman-token': "5e7c89a8-b4ef-088e-fc77-66a92e7f7b97"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    myweather = json.loads(response.text)

    tempIn = myweather['query']['results']['channel']['units']['temperature']
    speedIn = myweather['query']['results']['channel']['units']['speed']
    pressIn = myweather['query']['results']['channel']['units']['pressure']
    Title = myweather['query']['results']['channel']['title']
    temperature = myweather['query']['results']['channel']['item']['condition']
    atmosphere = myweather['query']['results']['channel']['atmosphere']
    wind = myweather['query']['results']['channel']['wind']
    presInHg = float(atmosphere['pressure']) * 0.0295299875

    wd = int(wind['direction'])

    if wd == 0:
        wdt = "North"
    elif wd == 90:
        wdt = "East"
    elif wd == 180:
        wdt = "South"
    elif wd == 270:
        wdt = "West"
    elif (wd > 0 and wd < 90):
        wdt = "North-East"
    elif (wd > 90 and wd < 180):
        wdt = "South-East"
    elif (wd > 180 and wd < 270):
        wdt = "South-West"
    else:
        wdt = "North-West"


    print("========================================================================")
    print("\nWeather for: {}".format(Title))
    print("Temperature is {} {}, with {} conditions".format(temperature['temp'],
                                tempIn, temperature['text']))
    print("Winds of {} {}, in direction {}".format(wind['speed'],
                                speedIn, wdt))
    print("Humidity is {}%, with atmospheric pressure of {:0.6} mBar\n".format(atmosphere['humidity'],
                                presInHg))
    print("========================================================================")

    #print(myweather)


def main():
    HOME = {"lat":"45.480270","lng":"-73.793137"}
    OFFICE = {"lat":"45.4879006","lng":"-73.7364181"}

    op = ""
    #Select home or office weather
    try:
        #op = int(input("Please select (1) for HOME or (2) for OFFICE ?"))
        op = input("Enter name of City: ")
    except ValueError:
        print("Please only use valid city names")
        raise SystemExit

    city = fc(op)
    lat = city.get_lat()
    lng = city.get_lng()
    if lat != '':
        querystring = {"lat":lat, "lng":lng}
        getWeather(querystring)
    else:
        querystring = HOME
        getWeather(querystring)


if __name__ == '__main__':
    main()
