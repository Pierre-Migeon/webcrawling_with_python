import scrapy
import pyodbc


class HousePriceSpider(scrapy.Spider) :
	name = "house_price_spider"
	start_urls = []
	
	connection = pyodbc.connect('DSN=pierres_sql_server;UID=sa;PWD=reallyStrongPwd123;')
	cursor = connection.cursor()
	
	for url in cursor.execute('SELECT * FROM websearch'):
		start_urls.append(url)

	define parse (self, response):
		pass
