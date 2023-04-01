import requests


def get_weather(location):

    url_template = 'http://wttr.in/{}?n?mTqu&lang=ru'
    url = url_template.format(location)
    response = requests.get(url)
    response.raise_for_status()

    return response.text


try:
    weather_forecast = get_weather('Лондон')
    print(weather_forecast)

    weather_forecast = get_weather('аэропорт Шереметьево')
    print(weather_forecast)

    weather_forecast = get_weather('Череповец')
    print(weather_forecast)
except requests.exceptions.HTTPError as error:
    exit("Can't get data from server:\n{0}".format(error))