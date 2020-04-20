import requests
from bs4 import BeautifulSoup
import json
import time
import re

# this is to gather all the URLs for the individual item pages.

all_data = []
item_counter = 1

# 498 products, defaults to 24 per page, so will need to loop through 21 pages
total_pages = range(0,1)

# i guess i'm gonna use a regex to help me pull out just the link?
url_pattern = re.compile(r'/([a-z]*-){1,5}[a-z]*')

# for every page in the total of 21 pages ...
for page_number in total_pages:

	url = 'https://www.seedsavers.org/department/vegetable-seeds?page='

	url = url + str(item_counter)

	print("Working on... ",url)

	page_request_results = requests.get(url)

	page_html = page_request_results.text

	soup = BeautifulSoup(page_html, "html.parser")

	# is this the right place to add 1 to the item_counter to advance the page #? is there a better spot?
	item_counter = item_counter+1

	# each url is in an a tag with a specific class. thank you for doing it like this, site
	all_as = soup.find_all("a", attrs = {'class':'facets-item-cell-grid-title'})

#print(all_as)

	# how do i make the all_as text?
	make_it_text = all_as.text
	just_url = url_pattern.findall(make_it_text)

print(just_url)
