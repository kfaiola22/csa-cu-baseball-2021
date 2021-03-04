# web scraping script attempt 2
# Rapsodo Data
# March 18, 2020

from bs4 import BeautifulSoup
import requests

# import csv
# csv_file = open('Rapsodo_scrape_data.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow([''])
#
#
# for __ in soup.findall():

source = requests.get('https://cloud.rapsodo.com/2.1/#/team-management').text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

body = soup.find('body')
# print(body.prettify())
