import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

url = "https://www.straitstimes.com/global"
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')
title_elements = soup.find_all('h5', class_='card-title')

for title_element in title_elements:
    title = title_element.find('a')  # Find the nested <a> tag
    if title:  # Check if the <a> tag exists
        print(title.text.strip())
