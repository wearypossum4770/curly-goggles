from pathlib import Path
from re import findall
from json import dumps
import requests

def get_icon_meta_data():
	_meta_data_regex = 'class\=\"(.*)\"\s+style.*\=\"(.*)\"\>\W+.*href\=\"(.*)\"\s+download\W+(\<svg.*\<\/svg\>)\s+.*(title)\"\>(.*)\<.*\s+.*\s+.*(subtitle)\"\>(.*)\<.*'
	_url_to_scrape = "https://simpleicons.org/"
	meta_data =[]
	npm_filename = Path.cwd().parent / "frontend" / "npm" / "src" / "icon_metadata.json"
	filename = Path('.') / "icon_metadata.json"
	resp = requests.get(_url_to_scrape).text
	_meta_data = findall(_meta_data_regex, resp)
	for icon in _meta_data:
		meta_data.append({
			"iconClassName":icon[0] ,
			"iconStyle":icon[1] , 
			"iconName":icon[5] ,
			"iconID":icon[7],
			"iconPath":icon[2],
			"iconURL": f"https://simpleicons.org{icon[2]}",
			"pathname": icon[2],
			"iconSVG":icon[3] ,
		})
	with open(filename, 'w') as f:
		f.write(dumps(meta_data))
	with open(npm_filename, 'w') as f:
		f.write(dumps(meta_data))
if __name__=='__main__':
	get_icon_meta_data()
