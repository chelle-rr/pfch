Some public libraries are adding seed libraries: patrons can request a seed, usually for an edible plant, from the library's catalog, grow it, and then "return" the seeds by donating seeds saved from the mature plant. Unlike most library materials, these seeds often don't have structured metadata; a list of seeds may just be available as a PDF or on a webpage, possibly with additional planting or historical info noted. This lack of structure is also evident across other groups, organizations, and businesses that share or sell heirloom seeds for edible gardens. There's a ton of info that would be both practical (like planting instructions) and interesting (any historical details) to have as structured data, for easy searching and organization. (Imagine you have a garden plot that only receives partial sunlight; being able to search your library's seed sharing catalog to find just the items that are good in partial sun would be extremely helpful.) For this project, I used the website of a non-profit organization that saves and sells rare and historic seed varieties, since it had a lot of information available that was only semi-structured. I scraped each individual seed page for information, then converted that info into a structured XML format, ready to be added to the catalog of some imaginary library and made searchable by patrons.

1_scrape_item_urls.py
This file searches each page of vegetable seeds on seedsavers.org to grab the URL for each individual seed. The URLs are stored in a json file called all_urls.json.

2_scrape_individual_pages.py
This file opens the all_urls.json and scrapes each page for certain info. After compiling that info into a dictionary for each URL, the info is stored in a json file called item_details.json.

3_json_to_xml.py
This file takes item_details.json and converts it into xml, since xml is more commonly used for metadata in libraries & archives. the output is called item_details_xml.xml.
