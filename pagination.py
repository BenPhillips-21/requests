import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'
response = requests.get(url)
page_html = response.text
soup = BeautifulSoup(page_html, 'html.parser')

page_count_string = soup.find('li', class_='current').text
page_count = int(page_count_string.strip().split(' ')[-1])
print(page_count)

# https://books.toscrape.com/catalogue/page-1.html

# If we know how many pages there are....

for page_no in range(1, page_count + 1):
    print(f'page --> {page_no}')
    page_url = f'https://books.toscrape.com/catalogue/page-{page_no}.html'
    response = requests.get(page_url)
    page_html = response.text
    soup = BeautifulSoup(page_html, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    print(len(books))

# If we don't know how many pages there are...

page_no = 45
while True:
    print(f'page --> {page_no}')
    page_url = f'https://books.toscrape.com/catalogue/page-{page_no}.html'
    response = requests.get(page_url)
    page_html = response.text
    soup = BeautifulSoup(page_html, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    print(len(books))

    # find the next button and if there isn't one then break from loop
    next_button = soup.find('li', class_='next')
    print(next_button)
    if next_button is None:
        break
    else:
        page_no += 1

