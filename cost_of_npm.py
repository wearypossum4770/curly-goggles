from pathlib import Path
from json import loads
import requests

base_url ='https://bundlephobia.com/scan'
package_json_path = Path.cwd() / 'gettingstarted/package.json'
def upload_package_json():
	with open(package_json_path,'rb') as opened_file:
		humanize = loads(opened_file.readlines())
	return humanize
	
# ~ req = requests.get(base_url, files=files)
	
# ~ <button class="scan__btn">Upload <code> package.json </code></button>
# ~ <button class="scan__btn">Scan 4 packages</button>a
# ~ <label><input type="checkbox" value="@testing-library/jest-dom#4.2.4"><span class="scan__package-item-title"><span>@testing-library/jest-dom</span><span class="scan__package-item-version">^4.2.4 → 4.2.4</span></span></label>
print(upload_package_json())
