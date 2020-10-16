import requests

longitude = -85.1819572
latitude = 35.0897734

url = f"https://api.weather.gov/points/{latitude},{longitude}"

def weather():
	resp = requests.get(url)
	return resp.text

print(weather())