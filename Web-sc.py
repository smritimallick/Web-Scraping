import requests
from bs4 import BeautifulSoup
import csv

# Using requests to extract the website
page = requests.get(
    "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")

soup = BeautifulSoup(page.content, 'html.parser')

# Empty list to append the required values from the website
c_laptops = []

# Extracting the required values from the website
computers = soup.select('div.thumbnail')

for laptop in computers:
    name = laptop.select('h4 > a')[0].text.strip()
    price = laptop.select('h4.price')[0].text.strip()
    r1 = str(laptop.select("div.ratings span"))
    ratings = r1.count("glyphicon-star")
    reviews = laptop.select('div.ratings')[0].text.strip()

# Appending the required values into the list
    c_laptops.append({
        "Product Name": name,
        "Product Price": price,
        "Ratings" : ratings,
        "Count of Reviews": reviews,
    })


keys = c_laptops[0].keys()

# Saving all the data into a csv file
with open('Web-scrape-Laptops.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(c_laptops)