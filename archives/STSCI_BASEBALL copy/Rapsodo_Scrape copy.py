# web scraping script attempt 2
# Rapsodo Data
# March 18, 2020

from bs4 import BeautifulSoup
import requests

# import csv
# csv_file = open('DPDough_Scrape.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['title', 'subtitle', 'days of the week', 'first week', 'second week', 'third week', 'fourth week', 'day number', 'zotd' ])
#
#
# for zotds in soup.findall():

source = requests.get('https://cloud.rapsodo.com/2.1/#/team-management').text
soup = BeautifulSoup(source, 'lxml')
