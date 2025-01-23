import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:134.0) Gecko/20100101 Firefox/134.0'}

book_dict = {
    'name': [],
    'price': [],
    'category': [],
    'stars': [],
    'upc': [],
    'availability': [],
    'in_stock': [],
    'image_link': []
}

def scrape_one_book(book_url):
  response = requests.get(book_url, headers=headers)
  response.encoding = 'utf-8'

  soup = BeautifulSoup(response.text, 'html.parser')

  # book name, price, category, stars, upc, availability, in_Stock, image_link

  # Get book title from main product div
  name = soup.find('div', class_='product_main').h1.text
  book_dict['name'].append(name)
  print(book_dict['name'])

  # Extract price from price element
  price = soup.find('p', class_='price_color').text
  book_dict['price'].append(price)
  print(price)

  # Find category by navigating breadcrumb list
  ul_container = soup.find('ul', class_='breadcrumb')
  li_items = ul_container.find_all('li')
  category = li_items[2].a.text
  book_dict['category'].append(category)
  print(category)

  # Dictionary to convert text ratings to numbers
  number_dict = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
  }

  # Get star rating by finding class name and converting to number
  star_p_element = soup.find('p', class_='star-rating')
  star_class_name_list = star_p_element['class']
  star_string = star_class_name_list[1]
  stars = number_dict[star_string]
  book_dict['stars'].append(stars)
  print(star_string)

  # Find UPC by locating header and getting sibling text
  upc_th = soup.find('th', string="UPC")
  chungus = upc_th.find_next_sibling().text
  book_dict['upc'].append(chungus)
  print(chungus)

  # Get availability text similarly
  avail_th = soup.find('th', string="Availability")
  avail = avail_th.find_next_sibling().text
  book_dict['availability'].append(avail)
  print(avail)

  # Extract number from availability text using string splitting
  in_stock = avail.split('(')[1].split(' ')[0]
  book_dict['in_stock'].append(in_stock)

  # Construct full image URL by combining base URL with image src
  img_link = "https://books.toscrape.com/" + soup.find('div', class_='thumbnail').img['src'][6:]
  book_dict['image_link'].append(img_link)
  with open('image_links.txt', 'a') as f:
    f.write(img_link +'\n')

  df = pd.DataFrame(book_dict)
  df.to_excel('book_info.xlsx', index=False)