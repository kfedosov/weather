import requests

URL_TEMPLATE = 'http://wttr.in/{}?nmMTqu&lang=ru'


def get_weather(location):
    url = URL_TEMPLATE.format(location)
    response = requests.get(url)
    response.raise_for_status()

    return response.text


if __name__ == "__main__":
    try:
        for site in ['Лондон', 'аэропорт Шереметьево', 'Череповец']:
            print(get_weather(site))
    except requests.exceptions.HTTPError as error:
        exit("Can't get data from server:\n{0}".format(error))
