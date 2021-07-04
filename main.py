# - *- coding: utf- 8 - *-

#Production by Famaxth
#Telegram - @por0vos1k


import config
import requests
from bs4 import BeautifulSoup


def parse():
    URL = config.url
    HEADERS = {
        'User-Agent': config.user_agent
    }

    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 's-item__wrapper clearfix')
    comps = []

    for item in items:
        comps.append({
            'title': item.find('h3', class_ = 's-item__title').get_text(strip = True),
            'price': item.find('span', class_ = 's-item__price').get_text(strip = True),
            'description': item.find('h3', class_ = 's-item__title').get_text(strip = True),
            'url': item.find('a', class_ = 's-item__link').get('href')
        })

        for comp in comps:
            print(f'Name: {comp["title"]}\nPrice: {comp["price"]}\nDescription: {comp["description"]}\nURL: {comp["url"]}\n\n\n')

parse() 
