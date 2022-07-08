from requests import Session
from bs4 import BeautifulSoup as BS
from time import sleep

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

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

