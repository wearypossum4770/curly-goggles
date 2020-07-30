import requests

url = "https://www.forbes.com/sites/ashleaebeling/2019/11/06/irs-announces-higher-estate-and-gift-tax-limits-for-2020/#5bffba572efb"
req = requests.get(url)
with open("website.html", "w") as f:
    f.write(req.text)
