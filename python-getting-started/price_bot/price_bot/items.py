# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class FloridaHillsNurseryItem(Item):
	product_name = Field()
	product_sku = Field()
	vendor_on_hand = Field()
	images = Field()
	images_url=Field()
	image_urls = Field()
	unit_price = Field()
	product_description = Field()
