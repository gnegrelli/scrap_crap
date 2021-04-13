import re
import scrapy

from bs4 import BeautifulSoup
from pathlib import Path


class MySpider(scrapy.Spider):
	name = 'my_spider'
	re_phone = re.compile(r'(\+\s*\d{1,3})?\s*(\(\s*\d{1,4}\s*\))?\s*([\d\- ]{6,})\b')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		filename = Path(kwargs.get('filename', ''))
		if filename.is_file():
			with open(filename, 'r') as f:
				self.start_urls = [url.strip() for url in f.read().split('\n') if url.strip()]
		self.start_urls = self.start_urls[:2]

	def parse(self, response):
		d = {'logos': [], 'phones': [], 'website': str(response.url)}
		soup = BeautifulSoup(response.body, features='lxml')
		text = re.sub(r'\s{2,}', ' ', soup.get_text().strip())
		phones = self.re_phone.findall(text)
		with open('/home/psiu/Desktop/crap.txt', 'a+') as f:
			print(text, file=f)
		d['phones'] = [
			phone.join(' ').strip() for phone in phones
		]
		d['logos'] = [
			img.attrib['src'] for img in response.css('img') if 
			any(re.search('logo', img.attrib.get(attr, ''), re.IGNORECASE) for attr in ('class', 'id', 'src', 'tag'))
		]
