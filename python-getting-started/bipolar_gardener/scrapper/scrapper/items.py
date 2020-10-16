from scrapy.item import Item, Field


class FloridaHillNurseryItem(Item):
	images = Field()
	last_updated = Field(serializer=str)
	product_vendor 	 = Field()
	product_id  = Field()
	product_category = Field()
	product_url  = Field()
	product_card = Field()
	vendor_published_date  = Field()
	vendor_date_modified  = Field()
	image_urls  = Field()
	product_description  = Field()
	product_price = Field()
	sales_tax = Field()
