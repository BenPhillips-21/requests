import requests
import os

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:134.0) Gecko/20100101 Firefox/134.0'}

def download_images():
    os.mkdir('book_images')

    with open('image_links.txt', 'r') as f:
        links_text = f.read()
        links_list = links_text.split('\n')
        print(links_list)

    for i, image_url in enumerate(links_list):
        if image_url:
            try:
                response = requests.get(image_url, headers=headers)
                with open(f'book_images/{i + 1}.jpg', 'wb') as image_file:
                    image_file.write(response.content)
            except Exception as e:
                print(f"Error downloading image {i + 1}: {e}")
                continue
        else:
            print("Invalid image URL found")
            break