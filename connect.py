import requests


# функция соединения
def connect_moex(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        raise ValueError
