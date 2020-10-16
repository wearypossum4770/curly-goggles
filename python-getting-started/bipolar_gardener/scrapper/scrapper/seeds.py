# ~ from scrapy.spiders import Spider
# ~ from scrapy.selector import Selector
# ~ import requests

# ~ _product_page_regex = 'href\W+(?P<navigation_link>(https.*\.asp)).*\"\>(?P<navigation_title>(\w+\s+\w+)).*|.*href\W+(?P<product_links>(https.*))\"\>(?P<product_type>(\w+\s+\w+)).*'
# ~ _product_type_regex='.*\"(?P<product_type>(\w+\s+\w+)).*href\=\"(?P<product_type_url>(http.*))\".*'
# ~ _category_page_regex = '.*title\=\"(?P<product_name>(.*))\"\s+class.*href\=\"(?P<product_type_url>(http.*))\".*'
# ~ _scrape_product_selection ='\<option.*\s+(.*)\s+\<\/option>'
# ~ _scrape_product_hidden_text = 'name\=\"(txtvariant)\".*\=\"(.*)\">'
# ~ _scrape_product_item_number = 'class\W+(plaintext)\W+(.*)\<\/td\>'


# ~ def scrape_home_page():
	# ~ url = 'https://www.burntridgenursery.com/mobile/'
	# ~ resp = requests.get(url).text
	# ~ resp_data = findall(_product_type_regex,resp)
	# ~ page_meta_data = dict([list([data[0],data[-1]]) for data in resp_data])
	# ~ start_urls = [data[-1] for data in resp_data]
	# ~ pp.pprint(page_meta_data)
	# ~ return start_urls


# ~ def scrape_next():
	# ~ start_urls = scrape_home_page()
	# ~ temp = []
	# ~ for url in start_urls:
		# ~ resp = requests.get(url).text
		# ~ resp_data = findall(_product_type_regex,resp)
		# ~ page_meta_data = dict([list([data[0],data[-1]]) for data in resp_data])

		# ~ meta = [data[-1] for data in resp_data]
		# ~ for next_meta in meta:
			# ~ temp.append(next_meta)
	# ~ return temp

	
# ~ class SeedsSpider(Spider):
    # ~ name = 'seeds'
    # ~ allowed_domains = ['burntridgenursery.com']
    # ~ start_urls = scrape_next()

    # ~ def parse(self, response):
        
