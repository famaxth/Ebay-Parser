


from bs4 import BeautifulSoup
import requests

def parse():
    URL = 'https://ru.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
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
