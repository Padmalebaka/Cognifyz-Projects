'''pip --version
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install requests
pip install beautifulsoup4
pip install requests beautifulsoup4'''
import requests
from bs4 import BeautifulSoup

def scrape_blog_titles(url):
    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the articles or posts (you'll need to know the structure of the website)
    articles = soup.find_all('article')

    # Extract and print the title and URL of each article
    for article in articles:
        title_tag = article.find('h2')
        if title_tag:
            title = title_tag.get_text(strip=True)
            link = title_tag.find('a')['href']
            print(f"Title: {title}\nURL: {link}\n")

def main():
    url = input("Enter the URL of the blog page to scrape: ")
    scrape_blog_titles(url)

if __name__ == "__main__":
    main()