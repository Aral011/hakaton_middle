import requests
from bs4 import BeautifulSoup as BS
import csv

BASE_URL = 'https://www.mashina.kg/'

def get_html(url):
    response = requests.get(url)
    return response.text

def get_soup(html):
    soup = BS(html, 'lxml')
    return soup

def get_car(soup):
    cars2 = soup.find('div', class_= 'table-view-list')
    cars = cars2.find_all('div', class_='list-item')
    for car in cars:
        title = car.find('h2', class_='name').text.strip()
        image = car.find('img', class_='lazy-image').get('data-src')
        price = car.find('div', class_='block price').find('strong').get_text(strip=True)
        info = car.find('div', class_='block info-wrapper item-info-wrapper').get_text(strip=True)
    
        write_csv({

            'title' : title,
            'image' : image,
            'price' : price,
            'info' : info
            
        })



def write_csv(data):
    with open('mashina.csv', 'a') as file:
        names = ['title', 'image', 'price', 'info']
        write = csv.DictWriter(file, delimiter=',', fieldnames=names)
        write.writerow(data)



def main():
    url = 'https://www.mashina.kg/search/all/#'
    html = get_html(url)
    soup = get_soup(html)
    get_car(soup)
main()

    
    

     
