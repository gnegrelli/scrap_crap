import re
import scrapy

from pathlib import Path


class MySpider(scrapy.Spider):
	name = 'my_spider'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		filename = Path(kwargs.get('filename', ''))
		if filename.is_file():
			with open(filename, 'r') as f:
				self.start_urls = [url.strip() for url in f.read().split('\n') if url.strip()]

	def parse(self, response):
		for img in response.css('img'):
			if any(re.search('logo', img.attrib.get(attr, ''), re.IGNORECASE) for attr in ('class', 'id', 'src', 'tag')):
				print(img.attrib['src'])
		print(50*'~')
