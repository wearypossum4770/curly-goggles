from json import load
from scrapy import Spider, Request, FormRequest
from pprint import PrettyPrinter

pp=PrettyPrinter(indent=4)
url ="https://www.chegg.com/auth?action=login&redirect=https%3A%2F%2Fwww.chegg.com%2Fsignout"
def authentication_failed(response):
	# TODO: Check the contents of the response and return True if it failed
	# or False if it succeeded.
	pass
class CheggBookSpider(Spider):
	name = 'ch'
	start_urls = [url]
		
	def parse(self, response):
		return FormRequest.from_response(
		response,
		formdata={"username":"wearypossum4770@yahoo.com","password":"C0unt3rP01s312!@"},
		callback = self.after_login
		)

		print("\n\n\n\n\n")
		pp.pprint(response)
		cookies = {
			'CSessionID':None,
			'user_geo_location':None,
			'PHPSESSID':None,
			}
	def after_login(self, response):
		if authentication_failed(response):
			self.logger.error("Login failed")
			return
