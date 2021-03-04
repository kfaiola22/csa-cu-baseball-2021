# web scraping script attempt 3
# Bagel Recipe!
# March 19, 2020

from bs4 import BeautifulSoup
import requests

# import csv
# csv_file = open('Everything_Bagel_Recipe.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow([''])
#
#
# for bagel in soup.findall():

source = requests.get('https://www.skinnytaste.com/easy-bagel-recipe/').text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

body = soup.find('body')
# print(body.prettify())
container = body.find('div', id='page_wrap', class_='container row')
# print(container.prettify())
wrap = container.find('div', class_='wrapper row')
# print
content = wrap.find('div', id='content')
post = content.find('div', class_='post single-post single-post-content')
recipe_container = post.find('div', id='wprm-recipe-container-47958')
recipe_template = recipe_container.find('div', class_='wprm-recipe wprm-recipe-template-skinnytaste')
summary = recipe_template.find('div', class_='wprm-recipe-summary wprm-block-text-italic').getText()
ingredients_container = recipe_template.find('div', class_='wprm-recipe-ingredients-container wprm-block-text-normal')
ingredients_header = ingredients_container.find('h3').getText()
ingr_group = ingredients_container.find('div', class_='wprm-recipe-ingredient-group')
ingrs_ul = ingr_group.find('ul', class_='wprm-recipe-ingredients')
print(ingrs_ul.find('li', class_='wprm-recipe-ingredient'))
for ingredient in ingrs_ul.findall('li', class_='wprm-recipe-ingredient'):
    amount = ingredient.find('span',class_='wprm-recipe-ingredient-amount').getText()
    unit = ingredient.find('span',class_='wprm-recipe-ingredient-unit').getText()
    name = ingredient.find('span',class_='wprm-recipe-ingredient-name').getText()
    print('repr(amount) + repr(unit) + repr(name)')

# ingrdnts = ingrs_ul.findall('li', class_='wprm-recipe-ingredient')
#
# print('DEBUG PART 2 ' + ingrdnts.prettify())
# ingrdnts_text = ingrdnts.findall('span').text
# print(ingrdnts_text.prettify())

#instructions_container = recipe_template.find('div', class_='wprm-recipe-instructions-container wprm-block-text-normal')
instructions_container = recipe_template.find('div', class_='wprm-recipe-instructions-container wprm-block-text-normal')
instructions_header = instructions_container.find('h3').text
ingr_group = ingredients_container.find('div', class_='wprm-recipe-ingredient-group')
ingrs_ul = ingr_group.find('ul', class_='wprm-recipe-ingredients')


# print(summary+ingredients_header+ingrdnts_text
