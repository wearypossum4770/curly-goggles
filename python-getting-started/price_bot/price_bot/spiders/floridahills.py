from pathlib import Path
from uuid import uuid4
from ..pre_scrape.florida_hill_nursery import pre_fetch_florida_hill_links
from scrapy import Spider, Request
from scrapy.linkextractors import LinkExtractor
from pprint import PrettyPrinter	
from price_bot.items import FloridaHillsNurseryItem
from .itmes import PriceBotItem
pp=PrettyPrinter(indent=4)
	
class FloridaHillsNurserySpider(Spider):
	name = 'fl'
	start_urls=pre_fetch_florida_hill_links()
	
	def parse(self, response):
		product_links = response.css('h2.fl-post-grid-title a::attr(href)').getall()
		yield from response.follow_all(product_links, self.parse_products)

	def parse_products(self, response):
		meta_data = {
			"unique_id": uuid4,
			"is_in_stock" : response.css('.in-stock::text').getall(),	
			"product_name" :response.css('.entry-title::text').getall(),
			"product_sku":response.css('.sku::text').getall(),
			"image_urls":response.css('.wp-post-image::attr(src)').getall(),
			"images_url":response.css('.wp-post-image::attr(srcset)').getall(),
			"unit_price":response.css('#prodpagemain bdi::text').getall(),
			"product_description":response.css('#tab-description > p::text').getall(),
		}

		# item = FloridaHillsNurseryItem()  

		# is_in_stock : response.css('.in-stock::text').getall()
		# product_name :response.css('.entry-title::text').getall()
		# product_sku:response.css('.sku::text').getall()
		# image_urls:response.css('.wp-post-image::attr(src)').getall()
		# images_url:response.css('.wp-post-image::attr(srcset)').getall()
		# unit_price:response.css('#prodpagemain bdi::text').getall()
		# product_description:response.css('#tab-description > p::text').getall()

		# item["product_name"]=product_name
		# item["product_sku"]=product_sku
		# item["vendor_on_hand"]=vendor_on_hand
		# item["images_url"]=images_url
		# item["image_urls"]=image_urls
		# item["unit_price"]=unit_price
		# item["product_description"]=product_description
		# print("\n\n\n\nItem is complete")
		# return item


	# def save_to_json(self)":
		# with open(f'{file_name}/florida_hill_meta_data.json','w') as post_scrape":
			# post_scrape.write(json.dumps(meta_data))
	
