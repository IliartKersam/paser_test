from multiprocessing.dummy import Array
from wsgiref import headers
import requests
from bs4 import BeautifulSoup as BS
from time import sleep

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

def download(url):
    """Функция загрузки изображений."""
    response = requests.get(url, stream=True)
    r = open('C:\\Dev\\image\\' + url.split('/')[-1], 'wb') #Не забудь указать актуальный путь!
    for value in response.iter_content(1048576):
        r.write(value)
    r.close()

#def get_url():
    """Функция получения карточек со всех страниц."""
    #for count in range(1, 8):
url= 'https://www.ozon.ru/category/smartfony-15502/apple-26303000/?sorting=price'
response = requests.get(url, headers=headers)
soup = BS(response.text, 'lxml')
print(soup)
data = soup.find_all('div', class_="w8j")
print(data)
#    for i in data:
#        card_url = 'https://ozone.ru' + i.find('div', class_='ju7').find('a').get('href')
#        yield card_url
#
#def array():
#    """Функция получения данных из каждой карточки."""
#    for card_url in get_url():
#        response = requests.get(card_url, headers=headers)
#        sleep(3)
#        soup = BS(response.text, 'lxml')
#        #data = soup.find('div', soup')
#        name = soup.find('div', 'data-widget="webProductHeading').find('div', class_='m4v').text
#        #price = data.find('h4').text
#        #text = data.find('p', class_='card-text').text
#        #url_img = 'https://scrapingclub.com' + data.find('img', class_='card-img-top img-fluid').get('src')
#        #download(url_img)
#        #yield name, price, text, url_img
#        print(name,'\n')
#
#array()
