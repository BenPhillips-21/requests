import requests
from bs4 import BeautifulSoup

# url = 'https://books.toscrape.com/'
#
# res = requests.get(url)
# print(res.status_code)
# print(res.text)
#
# page_html = res.text
#
# soup = BeautifulSoup(page_html, 'html.parser')
# print(soup.prettify())

# HOW TO SELECT ELEMENTS

quotes_url = 'http://quotes.toscrape.com/'

quotes_response = requests.get(quotes_url)
soupy = BeautifulSoup(quotes_response.text, 'html.parser')

title = soupy.find('title')
title_text = soupy.find('title').text
print(title)
print(title_text)

# selecting according to class name

first_quote = soupy.find('div', class_='quote')
print(first_quote)

all_quotes = soupy.find_all('div', class_='quote')
print(len(all_quotes))
print(all_quotes[4])

# selecting according to attributes

quote_text = first_quote.find('span', attrs={'itemprop': 'text'}).text
print(quote_text)

# selecting according to text inside of it

tags_title = soupy.find('h2', string='Top Ten tags')
print(tags_title)

# NAVIGATION BETWEEN ELEMENTS

tag_box = tags_title.parent
print(tag_box)

next_next_sibling = tags_title.find_next_sibling().find_next_sibling()
print(next_next_sibling)

previous_sibling = next_next_sibling.find_previous_sibling()
print(previous_sibling)

tag_children = tag_box.children
the_kids = list(tag_children)

for k in the_kids:
    print(k)

print(len(the_kids))
# removing new lines
final_kids = [x for x in the_kids if x!= '\n']

for k in final_kids:
    print(k)

print(len(final_kids))

# selecting an attribute on an element tag
top_tage_a = previous_sibling.a
#          notice the a here ^^^ which selects anchor element
top_tage_style = top_tage_a['style']
print(top_tage_style)
