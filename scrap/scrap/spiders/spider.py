import re
import scrapy


class MySpider(scrapy.Spider):
	name = 'my_spider'

	def start_requests(self):
		urls = [
#			'https://www.illion.com.au',
			'https://www.cialdnb.com/en',
			'https://www.cmsenergy.com/contact-us/default.aspx',
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		for img in response.css('img'):
			if any(re.search('logo', img.attrib.get(attr, ''), re.IGNORECASE) for attr in ('class', 'id', 'src', 'tag')):
				print(img.attrib['src'])
		print(50*'~')
