from unicodedata import category

import requests
from bs4 import BeautifulSoup

book_url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

response = requests.get(book_url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

# book name, price, category, stars, upc, availability, in_Stock, image_link

name = soup.find('div', class_='product_main').h1.text
print(name)

price = soup.find('p', class_='price_color').text
print(price)

ul_container = soup.find('ul', class_='breadcrumb')
li_items = ul_container.find_all('li')
category = li_items[2].a.text
print(category)

# returns list of class names
number_dict = {
   'One': 1,
   'Two': 2,
   'Three': 3,
   'Four': 4,
   'Five': 5
}

star_p_element = soup.find('p', class_='star-rating')
star_class_name_list = star_p_element['class']
star_string = star_class_name_list[1]
stars = number_dict[star_string]
print(stars)


upc_th = soup.find('th', string="UPC")
chungus = upc_th.find_next_sibling().text
print(chungus)

avail_th = soup.find('th', string="Availability")
avail = avail_th.find_next_sibling().text
print(avail)


in_stock = avail.split('(')[1].split(' ')[0]
print(in_stock)

# getting a property on an element
img_link = "https://books.toscrape.com/" + soup.find('div', class_='thumbnail').img['src'][6:]
print(img_link)