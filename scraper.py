import requests as req
from bs4 import BeautifulSoup

# Get whole HTML
page = req.get('https://www.pccomponentes.com/portatiles')

# Parse page content
parsed_page = BeautifulSoup(page.content, 'html.parser')

# Extract product data
products = parsed_page.find_all("div", {"class": "c-product-card__content"})

product_list = []

for product in products:
    # Get title
    header = product.find("header", {"class": "c-product-card__header"})
    header_h3 = header.find("h3", {"class": "c-product-card__title"})
    header_h3_a = header.find("a", {"class": "GTM-productClick enlace-disimulado"})
    title = header_h3_a.text

    print(header_h3_a.text)

    #< h3 class ="c-product-card__title" > < a class ="GTM-productClick enlace-disimulado" data-brand="Lenovo" data-category="Portátiles" data-id="313061" data-list="portatiles" data-loop="1" data-name='Lenovo Legion 5 15IMH05H Intel Core i7-10750H/16GB/512GB SSD/RTX2060/15.6"' data-price="1399" data-stock-web="1" href="/lenovo-legion-5-15imh05h-intel-core-i7-10750h-16gb-512gb-ssd-rtx2060-156" > Lenovo Legion 5 15IMH05H Intel Core i7-10750H / 16GB / 512GB SSD / RTX2060 / 15.6"</a></h3>


    break



# Crate CSV file


# Populate CSV