import requests
from bs4 import BeautifulSoup
import csv

link = 'https://market.isagha.com/prices'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

gold_details = []

def main_code():
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    golds = soup.find_all('li', {'class': 'prices-strip__tile'})

    for i in golds:
        gauge = i.find('span', {'class': 'prices-strip__name'}).text
        status = i.find('span', {'class': 'prices-strip__arrow'})['aria-label']  # ارتفاع / انخفاض
        sell_value = i.find('span', {'class': 'prices-strip__price--sell'}).find('span', {'class': 'prices-strip__value'}).text
        buy_value = i.find('span', {'class': 'prices-strip__price--buy'}).find('span', {'class': 'prices-strip__value'}).text

        gold_details.append({
            'العيار': gauge,
            'سعر البيع': sell_value,
            'سعر الشراء': buy_value,
            'الحالة': status,
        })


def printing():
    header = gold_details[0].keys()
    path = 'E:/isagha-gold-price-scraper/golds_prices.csv'
    with open(path, 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.DictWriter(file, header)
        writer.writeheader()
        writer.writerows(gold_details)
        print('file printed successfully')


main_code()
printing()