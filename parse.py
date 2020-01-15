#!/usr/bin/python3 

from bs4 import BeautifulSoup
from urllib.request import urlopen

link = "https://db.chgk.info/random/"

html_doc = urlopen(link).read()
soup = BeautifulSoup(html_doc, features="html.parser")


data = soup.find('div', 'random-results')

for block in data.find_all('div','random_question'):
    block.a.decompose()
    for s in block.strings:
        part = s.strip()
        if (len(part) > 0 and part != '...'):
            print(part)
    print()
