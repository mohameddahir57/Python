# Day 25 : Web Scraping (requests + BeautifulSoup) 
# Welcome to Day 26 of your Python learning journey! Today, we will explore web scraping using the `requests` library to fetch web pages and `BeautifulSoup` from the `bs4` module to parse HTML content. Web scraping allows you to extract data from websites for analysis or other purposes.
# Table of Contents
# 1. [Fetching a Web Page](#fetching-a-web-page)
# 2. [Parsing HTML with BeautifulSoup](#parsing-html-with-beautifulsoup)
# 3. [Practice Exercises](#practice-exercises)

# Fetching a Web Page
# To fetch a web page, you can use the `requests` library. Here's an example to fetch the HTML content of a web page:
import requests
url = "https://example.com"
response = requests.get(url)
html_content = response.text
print(html_content)  # This will print the HTML content of the page

# Parsing HTML with BeautifulSoup
# Once you have the HTML content, you can use `BeautifulSoup` to parse it and
# extract specific data. Here's an example of how to parse the HTML and extract all the links from the page:
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")
links = soup.find_all("a")
for link in links:
    print(link.get("href"))  # This will print the href attribute of each link

# Practice Exercises
# 1. Fetch the HTML content of a different web page (e.g., "https://news.ycombinator.com") and print it.
import requests
url = "https://news.ycombinator.com"
response = requests.get(url)
html_content = response.text
print(html_content)

# 2. Parse the HTML content of the fetched page and extract all the headlines (e.g., the text inside <a> tags with class "storylink").
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")
headlines = soup.find_all("a", class_="storylink")
for headline in headlines:
    print(headline.text)  # This will print the text of each headline

# 3. Extract and print all the URLs of the headlines you found in the previous exercise.
for headline in headlines:
    print(headline.get("href"))  # This will print the href attribute of each headline

# 4. Modify the code to extract and print the first 5 headlines and their URLs only.
for headline in headlines[:5]:
    print(f"Headline: {headline.text}")
    print(f"URL: {headline.get('href')}")
    print()  # Print a newline for better readability

