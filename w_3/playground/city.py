import pprint
import requests
from requests_oauthlib import OAuth1
from dateutil.parser import parse


class PogodaForecast:
    def get(self, city):
        cities = {"Уфа": '232968', "Стерлитамак": '232207',
                  "Москва": '13564', "Київ": '13088'
                  }
        domain = "http://api.yourweather.co.uk/index.php"
        query = {"api_lang": 'en',
                 "localidad": cities[city],
                 "affiliate_id": 'gd7khik781yp',
                 "v": '3.0'
                 }
        url = '{domain}?{urlencode(query)}'
        data = requests.get(url).json()
        forecast_data = data["query"]["results"]["channel"]["item"]["forecast"]
        forecast = []
        for day_data in forecast_data:
            forecast.append({
                "date": parse(day_data["date"]),
                "high_temp": day_data["high"]
            })
        return forecast


class YahooWeatherForecast(object):
    """docstring for YahooWeatherForecast"""

    def __init__(self, arg):
        super(YahooWeatherForecast, self).__init__()
        self.arg = arg

    def get(self, city):
        # данные для запроса
        format = 'json'
        unit = 'c'  # информация в градусах цельсия
        url = f'https://weather-ydn-yql.media.yahoo.com/forecastrss?location={city}&format={format}&u={unit}'

        # данные для аутентификации на сервере
        consumer_key = 'то что даст вам яху после регистрации'
        consumer_secret = 'то что даст вам яху после регистрации'

        print("sending http request...")
        auth = OAuth1(consumer_key, consumer_secret)
        data = requests.get(url, auth=auth).json()

        forecast = []
        # возвращаемый джейсон отличается от того что на видео,
        # здесь прогноз без вложенности, в корневом объекте
        forecast_data = data["forecasts"]
        for day_data in forecast_data:
            forecast.append({
                "day": day_data["day"],
                "high_temp": int(day_data["high"])
            })
#            print(day_data) # отладка: вывести полученный джейсон
        return forecas


class CityInfo:

    def __init__(self, city):
        self.city = city

    def weather_forecast(self):
        pass


def _main():
    city_info = CityInfo("Kyiv")
    forecaast = city_info.weather_forecast()
    pprint.pprint(forecaast)


if __name__ == "__main__":
    _main
