import requests as req
import csv
import time
from bs4 import BeautifulSoup

# Changing user agent
url = 'http://www.ichangtou.com/#company:data_000008.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
response = req.get(url, headers=headers)
# print(response.content)

search = ['https://www.pccomponentes.com/portatiles',
          'https://www.pccomponentes.com/portatil-acer',
          'https://www.pccomponentes.com/macbook,',
          'https://www.pccomponentes.com/portatil-asus',
          'https://www.pccomponentes.com/portatiles/coolbox',
          'https://www.pccomponentes.com/portatiles-dell',
          'https://www.pccomponentes.com/portatiles/dynabook-toshiba',
          'https://www.pccomponentes.com/portatiles/lg',
          'https://www.pccomponentes.com/portatiles-gaming',
          'https://www.pccomponentes.com/portatiles-lenovo']

product_list = []
i = 1

print('********** STARTING SCRAPING ********')

# Extract data from our url list
for page in search:
    # Get whole HTML
    page = req.get(page)

    # Parse page content
    parsed_page = BeautifulSoup(page.content, 'html.parser')

    # Extract product data
    products = parsed_page.find_all("div", {"class": "c-product-card__content"})

    name = ''
    price = 0
    availability = ''
    n_opinions = 0

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

        # Get img URL
        if title and price and availability and n_opinions:
            product_list.append([title, price, availability, n_opinions])

    print('DONE ITERATION :', i)
    i += 1
    # Sleeps for 30 sec to prevent get block
    print('SLEEPING FOR 15 SECONDS...')
    time.sleep(15)

# Crate CSV file
with open('hardware-store-data.csv', 'w' as file:
    print('********* CREATING CSV FILE ********')
    writer = csv.writer(file)
    headers = ['Product', 'Price', 'Availability', 'Number_of_opinions']
    writer.writerow(headers)

    # Populate CSV
    print('********* POPULATE CSV FILE ********')

    for product in product_list:
        writer.writerow(product)
