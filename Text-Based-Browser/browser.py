import sys
import os
from pathlib import Path
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Back, Style


def get_url_file(dir, url):
    url_key = url.replace(".", "_").replace("_com", "").replace("_org", "")
    return os.sep.join([dir, url_key + ".txt"])


def read_file(url):
    with open(get_url_file(dir, url), "r", encoding='UTF-8') as file:
        for line in file.readlines():
            print(line, end="")
        file.close()


def write_file(url, page):
    with open(get_url_file(dir, url), "w", encoding='UTF-8') as file:
        file.write(page)
        file.close()


def get_page(url):
    url_path = "http://" + url
    page = requests.get(url_path)
    soup = BeautifulSoup(page.content, 'html.parser')
    page = soup.find_all(text=True)

    output = ''
    whitelist = [
        'title',
        'p',
        'a',
        'ul',
        'ol',
        'li',
        'headers',
    ]

    for t in page:
        if t.parent.name in whitelist and len(t) > 1:
            if t.parent.name == 'a':
                print(Fore.BLUE + '{} '.format(t))
            else:
                print(Fore.BLACK + '{} '.format(t))
            output += '{} '.format(t)

    return output


if __name__ == '__main__':
    init()
    if len(sys.argv) > 1:
        dir = sys.argv[1]
        Path(dir).mkdir(parents=True, exist_ok=True)

    visited_pages = []
    url = input()

    while url != 'exit':
        if url == 'back':
            if len(visited_pages) > 0:
                url = visited_pages.pop(0)
                read_file(url)
        else:
            try:
                read_file(url)
                visited_pages.append(url)
            except FileNotFoundError:
                try:
                    output = get_page(url)
                    write_file(url, output)
                except Exception as e:
                    print("Error - invalid link")
                    print(e)

        url = input()

