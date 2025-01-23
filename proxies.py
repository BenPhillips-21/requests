import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:134.0) Gecko/20100101 Firefox/134.0'}

with open("proxies.txt", 'r') as p:
    proxy_string = p.read()
    proxy_list = proxy_string.split('\n')

for proxy in proxy_list:
    proxy_url = f'http://{proxy}'

    proxies = {
        'http': proxy_url,
        'https': proxy_url
    }

    url = 'http://books.toscrape.com'

    try:
        response = requests.get(url, headers=headers, proxies=proxies)

        if response.status_code == 200:
            print(f'Request is successful {proxy}')
        else:
            print(f'Request is unsuccessful {proxy}. Status code: {response.status_code}')
    except Exception as e:
        print(f'Request is unsuccessful {proxy}. Exception: {e}')
