from scrapy.spiders import Spider

class GitLabSpider(Spider):
	name = 'gitlab'
	start_urls = ['https://gitlab.com/users/sign_in']
	
	def parase(self, request):
		print('\n\n\n\n')
		print(request)
		print('\n\n\n\n')
