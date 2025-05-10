from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

url = 'https://www.olx.in/items/q-car-cover'
driver.get(url)
time.sleep(5)

soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

items = soup.find_all('li', class_='EIR5N')
results = []

for item in items:
    title_tag = item.find('span', class_='_2tW1I')
    price_tag = item.find('span', class_='_89yzn')
    if title_tag and price_tag:
        title = title_tag.text.strip()
        price = price_tag.text.strip()
        results.append(f'{title} - {price}')

with open('olx_car_covers.txt', 'w') as f:
    for line in results:
        f.write(line + '\n')
