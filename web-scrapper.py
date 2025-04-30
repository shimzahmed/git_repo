# A simple web scraper for kids to fetch article titles from a website
import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    try:
        # Send a request to the website
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find and print article titles (adjust the tag and class based on the website)
        print("Here are some cool article titles:")
        for title in soup.find_all('article', class_='product_pod'):  # Example: h2 with class 'title'
            print("- " + title.get_text(strip=True))
    except Exception as e:
        print(f"An error occurred: {e}")

def scrape_daraz_products(url):
    try:
        # Send a request to the website
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors

        #print(BeautifulSoup(response.text, 'html.parser').prettify)

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find and print product titles
        print("Here are some product titles from Daraz:")
        for product in soup.find_all('div', class_='Bm3ON'):  # Adjust class based on Daraz's structure
            print("- " + product.get_text(strip=True))
        
    except Exception as e:
        print(f"An error occurred: {e}")

# URL of a Daraz.pk category or search page
url = "https://books.toscrape.com/"  # Example: Search for "mobile"
scrape_titles(url)