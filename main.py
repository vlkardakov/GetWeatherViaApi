import requests
import json

def request_weather_api(url):
    requested = json.loads(requests.get(url).text)

    iii = 0

    days = {}
    for el in requested["forecast"]["forecastday"]:
        iii+=1
        days[f"day{iii}"] = {"date":el["date"], "min_temp":el["day"]["mintemp_c"], "max_temp":el["day"]["maxtemp_c"]}

    return days

if __name__ == "__main__":
    print(request_weather_api("https://api.weatherapi.com/v1/forecast.json?key=7fc288622be84864b63111704241212&q=Moscow&aqi=no&alerts=no&days=3"))