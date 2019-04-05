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


class YahooWeatherForecast:
    """docstring for YahooWeatherForecast"""

    def get(self, city):
        # данные для запроса
        format = 'json'
        unit = 'c'  # информация в градусах цельсия
        url = f'https://weather-ydn-yql.media.yahoo.com/forecastrss?location={city}&format={format}&u={unit}'
        # данные для аутентификации на сервере
        consumer_key = 'dj0yJmk9QnFRblJUckFBenNKJnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTVl'
        consumer_secret = 'bc99df9b9724f7e0ce029969868b8fd658dcb820'

        print("sending http request...")
        auth = OAuth1(consumer_key, consumer_secret)
        data = requests.get(url, auth=auth).json()

        forecast = []
        # возвращаемый джейсон отличается от того что на видео,
        # здесь прогноз без вложенности, в корневом объекте
        forecast_data = data["forecasts"]
        for day_data in forecast_data:
            forecast.append({
                "day": parse(day_data["day"]),
                "high_temp": int(day_data["high"])
            })
        print(day_data) # отладка: вывести полученный джейсон
        return forecast


class CityInfo:

    def __init__(self, city, forecast_provider=None):
        self.city = city
        self._forecast_provider = forecast_provider or YahooWeatherForecast()

    def weather_forecast(self):
        return self._forecast_provider.get(self.city)


def _main():
    city = CityInfo("Kiev")
    forecast = city.weather_forecast()
    pprint.pprint(forecast)


if __name__ == "__main__":
    _main()
