# Import necessary libraries to make the webscraping process a lot easier. "requests" is simply a library we can use to send HTTP requests using Python. BeautifulSoup is used for parsing HTML and XML documents.
import requests
from bs4 import BeautifulSoup

# This creates a dictionary named 'headers' with a single key-value pair. The key is "User-Agent" and the value is a string representing the browser's user agent. This is used to mimic a real browser request to bypass the Straits Times restrictions against web scrapers.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# The "url = " line basically initializes a variable named URL where we assign the URL of the website that we want to scrape.
# The "response = " line is to send a HTTP GET request to the specified 'url' using the 'requests.get()' method. 'headers' argument is passed to include the user agent in the request. And lastly the response from the server will be stored in the 'response' variable.
url = "https://www.straitstimes.com/global"
response = requests.get(url, headers=headers)

# 'html-parser' will parse the raw HTML content of the response using BeautifulSoup
# the soup.find_all will then search the parsed HTML for all <h5> elements with the class 'card-title'. I have already identified that all the articles have this title class.
soup = BeautifulSoup(response.content, 'html.parser')
title_elements = soup.find_all('h5', class_='card-title')

# This is a loop that will keep iterating over each 'title_element'. It first searches for the <a> tag within the current 'title_element'. If found, 'title.text' extracts the text content of the tag while 'strip() will get rid of any trailing whitespace.
for title_element in title_elements:
    title = title_element.find('a')  # Find the nested <a> tag
    if title:  # Check if the <a> tag exists
        print(title.text.strip())
