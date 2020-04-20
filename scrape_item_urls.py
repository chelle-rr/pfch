import requests
from bs4 import BeautifulSoup
import json
import time

# this is to gather all the URLs for the individual item pages.

all_data = []
item_counter = 1

# 498 products, defaults to 24 per page, so will need to loop through 21 pages
total_pages = range(0,21)

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

print(all_as)

	# get each url! th
	#for a_a in all_as:
	#	a_link =

		#all_li_el_in_div = a_div.find_all('li')

		#title_li = all_li_el_in_div[-1]

	#	a_link = title_li.find('a')

	#	title = a_link.text
	#	link = 'http://collection.mam.org/' + a_link['href']

	#	artwork = {
	#		"creators": creators,
	#		"title" : title,
	#		"url" : link
	#	}

	#	all_data.append(artwork)
		# print(title, link)
		# print(creator_stmts)
		# print('---')

#	item_counter = item_counter + 10


#	json.dump(all_data, open('artworks.json','w'), indent=2)

#	time.sleep(1)
