from re import findall
import requests


def pre_fetch_florida_hill_links():
	fetch_links = []
	home_page='https://floridahillnursery.com/plants/'
	pagination_regex = '<div class=\"fl-builder-pagination\">.*\s+.*\s+.*\s+.*\"\>(\d+).*\s+.*\s+.*\s+.*href\W+.*\"\>(\d+).*\s+.*\s+.*\s+\<\/div\>'
	print("sending request\n")
	resp = requests.get(home_page).text	
	_pagination = int(findall(pagination_regex, resp)[0][-1])
	urls = [f"{home_page}page/{page}" for page in range(2,_pagination+1)]
	urls.append(home_page)
	return urls
