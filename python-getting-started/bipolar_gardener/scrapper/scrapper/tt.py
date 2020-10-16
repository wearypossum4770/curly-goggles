from re import findall 
from urllib.parse import unquote
import requests
from pprint import PrettyPrinter	
home_page='https://floridahillnursery.com/plants/'
_link_extractor_regex= 'href\=\"(https:\/\/\w+.com.*\/)\".*title\=\"(.*)\"\>\s+.*src\=\"(.*)\"\s+alt.*'
_price_information = 'price.*(\$).*\>(\d+.\d+).*(sales tax)'

_product_grid = 'href\=\"(https:\/\/\w+.com.*\/)\".*title\W+(.*)\"\>\s+.*src\=\"(.*)\"\s+alt.*\s+.*\s+.*\s+.*\s+.*\s+.*\s+.*\s+.*(\$)\W+\w+\>(\d+.\d+).*(sales tax).*'
_pagination_regex = '<div class=\"fl-builder-pagination\">.*\s+.*\s+.*\s+.*\"\>(\d+).*\s+.*\s+.*\s+.*href\W+.*\"\>(\d+).*\s+.*\s+.*\s+\<\/div\>'
pp = PrettyPrinter(indent=4)

def scrape():
	resp = requests.get(home_page).text
	_home_page = findall(_product_grid,resp)
	_pagination = int(findall(_pagination_regex, resp)[0][-1])
	# ~ for page in range(2,_pagination+1):
		# ~ f"{home_page}page/{page}"
		# ~ resp = requests.get(f"{home_page}page/{page}").text
		# ~ _other_pages = findall(_product_grid,resp)
		# ~ pp.pprint(_other_pages[0])
	pp.pprint( _home_page)

scrape()

# ~ _product_grid = 'href\=\"(https:\/\/\w+.com.*\/)\".*title\W+(.*)\"\>\s+.*src\=\"(.*)\"\s+alt.*'
# ~ home_page='https://floridahillnursery.com/plants/'

# ~ def homepage():
	# ~ _pagination_regex = '<div class=\"fl-builder-pagination\">.*\s+.*\s+.*\s+.*\"\>(\d+).*\s+.*\s+.*\s+.*href\W+.*\"\>(\d+).*\s+.*\s+.*\s+\<\/div\>'
	# ~ resp = requests.get(home_page).text
	# ~ _home_page = findall(_product_grid,resp)
	# ~ _pagination = int(findall(_pagination_regex, resp)[0][-1])
	# ~ start_urls = [f"{home_page}page/{page}" for page in range(2,_pagination+1)]
	# ~ start_urls.append(home_page)
	# ~ pp.pprint(start_urls)
# ~ homepage()
