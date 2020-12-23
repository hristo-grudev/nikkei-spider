import scrapy

from scrapy.loader import ItemLoader

from scrapy.linkextractors import LinkExtractor
from scrapy.utils.markup import remove_tags
from nikkei.items import NikkeiItem


class NikkeiSpider(scrapy.Spider):
	name = 'nikkei'
	allowed_domains = ['www.nikkei.com']
	start_urls = ['https://www.nikkei.com/access/index/?bd=hKijiSougou']
	days_page = LinkExtractor(restrict_xpaths='//h2/div/div[2]/ul/li/a')
	news_page = []

	def parse(self, response):
		self.news_page = LinkExtractor(restrict_xpaths='//span[@class="m-miM32_itemTitleText"]/a')
		days_page_links = self.days_page.extract_links(response)
		yield from response.follow_all(days_page_links, self.parse_article)

	def parse_article(self, response):
		news_page_links = self.news_page.extract_links(response)
		yield from response.follow_all(news_page_links, self.parse_news)

	def parse_news(self, response):

		title = response.xpath("//header/hgroup/h1/text()").get()
		description = response.xpath('//article/section[1]').getall()
		date = response.xpath("(//time)[1]/text()").get()
		if description:
			description = remove_tags(str(description[0]))

		item = ItemLoader(item=NikkeiItem(), response=response)
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
