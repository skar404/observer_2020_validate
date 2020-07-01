import argparse

from download.main import download_files, archive_files


def app():
    parser = argparse.ArgumentParser()

    parser.add_argument('command')

    args = parser.parse_args()
    c = args.command

    if c == 'download':
        download_files()
    elif c == 'archive':
        archive_files()


if __name__ == '__main__':
    app()
