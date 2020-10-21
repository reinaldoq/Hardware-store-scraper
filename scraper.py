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
    header_h3_a = header_h3.find("a", {"class": "GTM-productClick enlace-disimulado"})
    title = header_h3_a.text

    # Get price
    div_price_1 = product.find('div', {"class": "c-product-card__prices cy-product-price"})
    div_price_2 = div_price_1.find('div', {"class": "c-product-card__prices-actual c-product-card__prices-actual--discount cy-product-price-discount"})
    if div_price_2:
        span_price = div_price_2.find('span')
        price = span_price.text


# Crate CSV file


# Populate CSV