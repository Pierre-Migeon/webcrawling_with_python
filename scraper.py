import scrapy


class HousePriceSpider(scrapy.Spider) :
	name = "house_price_spider"
	start_urls = ['http://www.vitalsigns.mtc.ca.gov/home-prices']




