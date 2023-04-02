import requests

URL_TEMPLATE = 'http://wttr.in/{}'
PAYLOAD = 'nMTq&lang=ru'


def get_weather(location):
    url = URL_TEMPLATE.format(location)
    response = requests.get(url, params=PAYLOAD)
    response.raise_for_status()

    return response.text


if __name__ == "__main__":
    try:
        weather_in_london = get_weather('Лондон')
        weather_in_svo: str = get_weather('аэропорт Шереметьево')
        weather_in_cherepovets = get_weather('Череповец')
    except requests.exceptions.HTTPError as error:
        exit("Can't get data from server:\n{0}".format(error))

    print(weather_in_london)
    print(weather_in_svo)
    print(weather_in_cherepovets)
