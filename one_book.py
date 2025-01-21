import requests
from bs4 import BeautifulSoup

book_url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

response = requests.get(book_url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

# book name, price, category, stars, upc, availability, in_Stock, image_link

# Get book title from main product div
name = soup.find('div', class_='product_main').h1.text
print(name)

# Extract price from price element
price = soup.find('p', class_='price_color').text
print(price)

# Find category by navigating breadcrumb list
ul_container = soup.find('ul', class_='breadcrumb')
li_items = ul_container.find_all('li')
category = li_items[2].a.text
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
print(stars)

# Find UPC by locating header and getting sibling text
upc_th = soup.find('th', string="UPC")
chungus = upc_th.find_next_sibling().text
print(chungus)

# Get availability text similarly
avail_th = soup.find('th', string="Availability")
avail = avail_th.find_next_sibling().text

# Extract number from availability text using string splitting
in_stock = avail.split('(')[1].split(' ')[0]
print(in_stock)

# Construct full image URL by combining base URL with image src
img_link = "https://books.toscrape.com/" + soup.find('div', class_='thumbnail').img['src'][6:]
print(img_link)