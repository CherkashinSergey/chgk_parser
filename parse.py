#!/usr/bin/python3 

from bs4 import BeautifulSoup
from urllib.request import urlopen

link = "https://db.chgk.info/random/"

html_doc = urlopen(link).read()
soup = BeautifulSoup(html_doc, features="html.parser")


data = soup.find('div', 'random-results')

for block in data.find_all('div','random_question'):
    source = block.a
    quest_header_block = block.find('strong')
    question_header = quest_header_block.string
    question_body = block.strong.next_element.next_element
    question_body = question_body.strip()


    answer_block = block.find('div','collapsible collapsed')
    answer_body = answer_block.strong.next_element.next_element

    full_answer = ''
    for s in answer_block.strings:
        part = s.strip()
        if (len(part) > 0 and part != '...'):
            full_answer += part
            full_answer += '\n'
    full_answer = full_answer.strip()

    print(question_header)
    print(question_body)
    print(full_answer)
    print()
