import requests
from bs4 import BeautifulSoup


def wrap(text: str):
    new_text = ['']

    for word in text.split(' '):
        if len(new_text[-1]) + len(word) + 1 > 80:
            new_text.append('')

        new_text[-1] += ' '
        new_text[-1] += word

    return '\n'.join(new_text)


def main():
    url = 'https://lenta.ru/news/2021/10/29/memory/'
    response = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page, features='html.parser')
    print(wrap(soup.text))


if __name__ == '__main__':
    main()
