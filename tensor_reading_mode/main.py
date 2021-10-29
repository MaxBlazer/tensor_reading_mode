import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://lenta.ru/news/2021/10/29/memory/'
    response = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page)
    ...


if __name__ == '__main__':
    main()
