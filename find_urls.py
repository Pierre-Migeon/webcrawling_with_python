import os

'''
This portion finds URLs that may contain information about housing prices in the San Francisco Bay area and stores them in a textfile.
'''

try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found, trying to download now")
	os.system("pip3 install beautifulsoup4")
	os.system("pip3 install google")

# to search
query = "Bay Area Housing Prices"
file = open("urls.txt", "w")

for j in search(query, tld="com", lang='en', num=10, pause = 2.0):
	file.write(j + "\n")

file.close()
