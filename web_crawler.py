import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
url = "https://www.pascalcoste-shopping.com/esthetique/fond-de-teint.html"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')


def scrape_product_info(url):
    # Define user-agent headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    page = 1
    products = []
    while page:
      # Send GET request to the URL
      response = requests.get(url+"?p="+str(page), headers=headers)

      # Parse the HTML content
      soup = BeautifulSoup(response.content, 'html.parser')



      # Extract product details
      product_elements = soup.find("div", id='uk-product-list-container').find_all("div", class_="uk-panel uk-position-relative")

      print(f"Found {len(product_elements)} product(s) on the page.")
      if len(product_elements) == 0:
        break
      for product in product_elements:
          name_element = product.find('h3', class_='product-name uk-margin-top')
          price_element = product.find('span', class_='uk-price')
          brand_element = product.find("div", class_="uk-position-relative").find("div", class_="uk-width-expand")
          prod_url_element = product.find('a', class_='uk-position-cover uk-cover-link-product')['href']
          img_url_element = soup.find('img', class_='product-image-photo')['src']

          if name_element is not None and price_element is not None:
              name = name_element.text.strip()
              price = float(price_element.text.replace('€', '').strip().replace(',', '.'))
              brand = brand_element.text
              prod_url = prod_url_element
              img_url = img_url_element

              product_info = {
                  'name': name,
                  'price': round(price, 2),
                  'brand': brand,
                  'prod_url': prod_url,
                  'img_url': img_url,
              }

              products.append(product_info)
          else:
              print("Could not find name or price element for a product.")
      page += 1

    print(len(products))
    return products

url = 'https://www.pascalcoste-shopping.com/esthetique/fond-de-teint.html'
products_info = scrape_product_info(url)
print(products_info)


#Database creation 
# Function to save extracted product information to a JSON file
import json
def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":

    save_to_json(products_info, 'products.json')


import sqlite3
import json

# Function to create database tables
def create_tables():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Create products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price REAL,
            brand TEXT,
            imageUrl TEXT,
            productUrl TEXT
        )
    ''')

    conn.commit()
    conn.close()



