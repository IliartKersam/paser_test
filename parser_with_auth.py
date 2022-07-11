from requests import Session
from bs4 import BeautifulSoup as BS
from time import sleep

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

def array():
    work = Session()
    work.get('https://quotes.toscrape.com/', headers=headers)
    response = work.get('https://quotes.toscrape.com/login', headers=headers)
    soup = BS(response.text, 'lxml')
    csrf_token = soup.find('form').find('input').get('value')
    data = {
        "csrf_token": csrf_token,
        "username": "Nick",
        "password": "password"
    }
    response = work.post('https://quotes.toscrape.com/login', headers=headers, data=data, allow_redirects=True)
    page = 1
    while page != False:
        response = work.get(f'http://quotes.toscrape.com/page/{page}/')
        soup = BS(response.text, 'lxml')
        data = soup.find_all('div', class_='quote')
        if len(data) != 0:
            for elem in data:
                text = elem.find('span', class_='text').text
                author = elem.find('span', class_='').find('small', class_='author').text
                goodreads_page = elem.find('span', class_='').find_all('a')[-1].get('href')
                yield text, author, goodreads_page
            page += 1
        else:
            page = False
