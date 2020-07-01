import requests

from download.const import FILES_LIST
from config import BACK_UP_DIR

URL = 'https://observer2020.mos.ru/observer/downloads/{file}'


def download(date_time) -> requests.Response:
    req = requests.get(url=URL.format(file=date_time))
    return req


def save_file(file_name: str, r: requests.Response):
    with open(BACK_UP_DIR + file_name, 'wb') as f:
        f.write(r.content)


def main():
    for file in reversed(FILES_LIST):
        save_file(file, download(file))


if __name__ == '__main__':
    main()
