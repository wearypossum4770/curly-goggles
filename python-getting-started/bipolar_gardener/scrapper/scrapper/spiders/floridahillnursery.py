from re import findall 
from datetime import datetime
from scrapy import Spider, Request
import requests
from scrapper.items import FloridaHillNurseryItem
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=4)

def gather_all_links():
	home_page='https://floridahillnursery.com/plants/'
	_pagination_regex = '<div class=\"fl-builder-pagination\">.*\s+.*\s+.*\s+.*\"\>(\d+).*\s+.*\s+.*\s+.*href\W+.*\"\>(\d+).*\s+.*\s+.*\s+\<\/div\>'
	resp = requests.get(home_page).text
	_pagination = int(findall(_pagination_regex, resp)[0][-1])
	urls = [f"{home_page}page/{page}" for page in range(2,_pagination+1)]
	urls.append(home_page)
	good_links = [link for link in urls if link.startswith('https')]
	return good_links
class FloridaHillNurserySpider(Spider):
	name = 'flhill'

	def start_requests(self):
		urls = gather_all_links()
		urls = 
		for url in urls:
			yield Request(url=url, callback=self.parse)

	def parse(self, response):
		"""
		Request Keys 
			status, request, ip_address, flags
			certificate, _url, _encoding
			headers: [
				'Accept-Ranges', 'Age', 'Content-Security-Policy'
				'Content-Type', 'Date', 'Server',
				'Strict-Transport-Security', 'Vary', 'X-Backend',
				'X-Cache', 'X-Cache-Hit','X-Cacheable',
				'X-Content-Type-Options', 'X-Xss-Protection',
				]
			
		"""

		# ~ product.add_css('product_vendor', 'meta[content="Florida Hill Nursery"]::attr(content)')
		# ~ product.add_css( 'product_id','.product_type_simple::attr(data-product_id)' )
		# ~ product.add_css('product_category' ,'.product_type_simple::attr(data-product_sku)' )
		# ~ product.add_css('product_url' , '.product_type_simple::attr(href)')
		# ~ product.add_css('vendor_published_date' , 'meta[itemprop="datePublished"]::attr(content)')
		# ~ product.add_css('vendor_date_modified' ,'meta[itemprop="dateModified"]::attr(content)' )
		# ~ product.add_css('image_urls' ,'.no-lazyload::attr(src)' )
		# ~ product.add_css('product_description' , '.fl-post-grid-title a::text')
		# ~ product.add_css('product_price' ,'.amount::text' )
		# ~ product.add_css('sales_tax' ,len('.woocommerce-price-suffix::text')>1 )
		# ~ return product.load_item()

		# ~ product.add_css('' , )
		product = FloridaHillNurseryItem(
		product_vendor = response.css('meta[content="Florida Hill Nursery"]::attr(content)').extract(),		
		product_id = response.css('.product_type_simple::attr(data-product_id)').extract(),
		product_category = response.css('.product_type_simple::attr(data-product_sku)').extract(),
		product_url = response.css('.product_type_simple::attr(href)').extract(),
		# ~ product_card = response.css('.fl-post-column').extract(),
		vendor_published_date = response.css('meta[itemprop="datePublished"]::attr(content)').extract(),
		vendor_date_modified = response.css('meta[itemprop="dateModified"]::attr(content)').extract(),
		image_urls = response.css('.no-lazyload::attr(src)').get(),
		product_description = response.css('.fl-post-grid-title a::text').extract(),
		product_price =  response.css('.amount::text').extract(),
		sales_tax = len(response.css('.woocommerce-price-suffix::text').extract())>1,
)
		# ~ product_vendor = findall('' ,response.body)		
		# ~ product_id = findall('' ,response.body)
		# ~ product_category =findall('' ,response.body)
		# ~ product_url = findall('' ,response.body)
		# ~ product_card = findall('' ,response.body)
		# ~ vendor_published_date = findall('' ,response.body)
		# ~ vendor_date_modified = findall('' ,response.body)
		# ~ image_urls = findall('' ,response.body)
		# ~ product_description = findall('property\W+og:title\"\s+\w+\W+(.*)\|',str(response.body))
		# ~ product_price =  findall('' ,response.body)
		# ~ sales_tax = findall('' ,response.body)

		# ~ individual_product = dict([
			# ~ ['product_vendor',product_vendor],
			# ~ ['product_id',product_id],
			# ~ ['product_category',product_category],
			# ~ ['product_url',product_url],
			# ~ ['vendor_published_date',vendor_published_date],
			# ~ ['vendor_date_modified',vendor_date_modified],
			# ~ ['image_urls',image_urls],
			# ~ ['product_description',product_description],
			# ~ ['product_price',product_price],
			# ~ ['sales_tax',sales_tax],
			# ~ ])


		pp.pprint(product)

		# ~ product['product_vendor'] =  product_vendor 
		# ~ product['product_id'] =  product_id 
		# ~ product['product_category'] =  product_category 
		# ~ product['product_url'] =  product_url 
		# ~ product['vendor_published_date'] =  vendor_published_date 
		# ~ product['product_card'] =  product_card 
		# ~ product['vendor_published_date'] = vendor_published_date  
		# ~ product['vendor_date_modified'] = vendor_date_modified  
		# ~ product['image_urls'] =image_urls   
		# ~ product['product_description'] =product_description 
		# ~ product['product_price'] =product_price 
		# ~ product['sales_tax'] =sales_tax 

