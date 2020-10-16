from pathlib import Path
import json
file_name = Path('/home/gatorcollege2006/web_dev/python-getting-started/price_bot/price_bot') / "works_cited.json" 
def that():
	with open(file_name, 'rw') as f:
		data = json.loads(f)
	return data
print(that())
