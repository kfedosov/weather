import requests

URL_TEMPLATE = 'http://wttr.in/{}'
PAYLOAD = {'lang': 'ru', 'nMTq' : None}
PAYLOAD = '&'.join([key if value is None else f"{key}={value}" for key,
                                                    value in PAYLOAD.items()])


def get_weather(location):
    url = URL_TEMPLATE.format(location)
    try:
        response = requests.get(url, params=PAYLOAD)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f"Can't get data for {location}: {e}"
    else:
        return response.text


if __name__ == "__main__":
    locations = ['Лондон', 'аэропорт Шереметьево', 'Череповец']
    for location in locations:
        weather = get_weather(location)
        print(weather)
