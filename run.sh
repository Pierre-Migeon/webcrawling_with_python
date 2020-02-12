#########################
# Playing with data...	#
#	Pierre Migeon	#
#########################
URL_FILE="./urls.txt"

#If there are no urls...
if [ ! -f $URL_FILE ] || [ ! -s $URL_FILE ]; then
	python3 find_urls.py
fi;

#if there still aren't URLs, then exit... 
if [ ! -f $URL_FILE ] ||  [ ! -s $URL_FILE ]; then
	echo "There was a problem creating the list of URLs. Something went wrong, exiting..." && exit 1
fi;

#If there's nothing in the database, then make the database
TEST=`python3 testdb.py | wc -l`
if [ $TEST == "0" ]; then
	python3 makedb.py
fi;

#If there's still nothing in the database, something went wrong and we'll exit.
TEST=`python3 testdb.py | wc -l`
if [ $TEST == "0" ]; then 
	echo "There were no entries in the url database. Something went wrong... exiting now..." && exit 1;
fi;

scrapy runspider scraper.py

