import re

import requests
from bs4 import BeautifulSoup, Tag
import argparse


def wrap(text: str):
    new_text = ['']

    for word in text.split(' '):
        if len(new_text[-1]) + len(word) + 1 > 80:
            new_text.append('')

        new_text[-1] += ' '
        new_text[-1] += word

    return '\n'.join(new_text)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    args = parser.parse_args()

    response = requests.get(args.url)
    page = response.text
    soup = BeautifulSoup(page, features='html5lib')

    soup = soup.body

    if soup.main is not None:
        soup = soup.main

    if soup.article is not None:
        soup = soup.article

    ignored_tags = ['nav', 'script', 'style', 'meta', 'time', 'aside', 'header', 'footer']

    ignored_classes = [
        re.compile('.*header.*'),
        re.compile('.*sidebar.*'),
        re.compile('.*footer.*'),
    ]

    for tag_name in ignored_tags:
        for tag in soup.find_all(tag_name):
            tag.extract()

    for class_ in ignored_classes:
        for tag in soup.find_all(class_=class_):
            tag.extract()

    for tag in soup.find_all(style="display: none;"):
        tag.extract()

    def estimator(tag):
        return len([child for child in tag.children if child.name == 'p'])

    article = max(soup.find_all('div'), key=estimator)

    allowed_children = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']

    for child in article.children:
        if isinstance(child, Tag) and child.name not in allowed_children:
            child.extract()

    for a in article.find_all('a'):
        a.replace_with(f"{a.text} [{a['href']}]")

    result = '\n\n'.join(wrap(child.text) for child in article.children if isinstance(child, Tag))

    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write(result)


if __name__ == '__main__':
    main()
