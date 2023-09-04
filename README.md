# Simple Web Scraper

This project documents my journey in building a web scraper using Python. I am fairly new to programming in Python (and actually programming in general) and wanted to learn Python by trying to build something that helps to solve real-life problems. In the past year, I have constantly been looking at car listings in Los Angeles on FB Marketplace and Craigslist as I had dreams of upgrading my car. Now that I'm heading back to Singapore, that use case is no longer relevant, but I decided that I still want to try building a web scraper. 

Thus, I pivoted my goal to scrape listings from Carousell, but due to various challenges, I shifted to scraping articles from The Straits Times.

## Journey

I started with the intention to scrape Carousell listings of the "4080" search page using **Beautiful Soup**. However, I soon realized the following:

- Carousell's page had dynamic content loaded via JavaScript, so I needed **Selenium**.
- To use Selenium, I had to download the ChromeDriver.
- The ChromeDriver version had to match my Chrome browser's version. but ChromeDriver hadn't released the most updated version that was compatible with Chrome's latest version. 
- I opted for a WebDriver manager to handle the driver versioning.
- Even with Selenium, I couldn't retrieve data from Carousell due to changing CSS classes and other complexities.

After these challenges, I decided to scrape a simpler site: The Straits Times. The titles on this site had a consistent CSS class, making the scraping process more straightforward.

## Challenges & Solutions

1. **Dynamic Content on Carousell**: I learned about the difference between static and dynamic websites. For dynamic sites like Carousell, where content is loaded via JavaScript, tools like Selenium are essential.

2. **ChromeDriver Versioning**: I faced issues with ChromeDriver's version not matching my browser's version. The solution was to use a WebDriver manager that automatically manages driver versions.

3. **Anti-Scraping Mechanisms**: Some websites employ measures to block or limit scrapers. I overcame this by setting a user-agent in the request headers to mimic a real browser request. This worked when I tried to scrape the Straits Times. 

## Key Learnings

- **Requests Library**: This Python library is essential for making HTTP requests. Without it, the code would throw a `NameError`.
  
- **Parsing with BeautifulSoup**: Parsing means analyzing a string (like HTML) to determine its structure. BeautifulSoup, created by Leonard Richardson, makes this process easier in Python.

- **User-Agent**: Websites can identify and block scrapers. By setting a user-agent, we can mimic a real browser and bypass some of these restrictions.

- **Python Syntax**: Understanding Python's syntax, like how to use methods and attributes, is crucial. For instance, `soup.find_all` is a method provided by BeautifulSoup to find all matching tags.

## Conclusion

I thought that it would be really simple to build a webscraper but I didn't expect that there would be so many unforeseen circumstances. I also learnt from experienced programmer friends that typically webscrapers encounter other issues like Captcha and API throttling which could make things even more complex. 
