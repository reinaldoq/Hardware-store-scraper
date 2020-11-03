import requests as req
import csv
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
    div_price_2 = div_price_1.find('div', {
        "class": "c-product-card__prices-actual c-product-card__prices-actual--discount cy-product-price-discount"})
    if div_price_2:
        span_price = div_price_2.find('span')
        price = span_price.text

    # Get availability
    div_availability = product.find('div', {
        "class": "c-product-card__availability disponibilidad-inmediata cy-product-availability-date"})
    if div_availability:
        div_availability_strong = div_availability.find('strong')
        availability = div_availability_strong.text

    # Get rating and opinions
    div_rating = product.find('div', {"class": "c-star-rating cy-product-rating"})
    if div_rating:
        div_rating_div = div_rating.find('span')
        rating = div_rating_div.text
        div_opinions_span = div_rating.find('span', {'class': "c-star-rating__text cy-product-rating-result"})
        n_opinions = div_opinions_span.text

    product_list.append([title, price, availability, n_opinions])

# Crate CSV file
with open('hardware-store-data.csv', 'w') as file:
    writer = csv.writer(file)
    headers = ['Product', 'Price', 'Availability', 'Number_of_opinions']
    writer.writerow(headers)

    # Populate CSV
    for product in product_list:
        writer.writerow(product_list)
