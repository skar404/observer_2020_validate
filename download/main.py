from zipfile import ZipFile, ZIP_LZMA, ZIP_BZIP2

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


def archive_f(file):
    file_path = BACK_UP_DIR + file

    with ZipFile(file_path + '.zip', 'w', ZIP_LZMA) as f:
        f.write(file_path, file)


def archive_files():
    for file in reversed(FILES_LIST):
        archive_f(file)
        print('archive file:', file)


def download_files():
    for file in reversed(FILES_LIST):
        save_file(file, download(file))
        print('download and save file:', file)


if __name__ == '__main__':
    download_files()
