import os
import pyodbc

#Open connection to SQL server
connection = pyodbc.connect('DSN=pierres_sql_server;UID=sa;PWD=reallyStrongPwd123')
#Create cursor object
cursor = connection.cursor()

#Create fresh table
cursor.execute('DROP TABLE IF EXISTS websearch')
cursor.execute("""IF object_id('websearch', 'U') is null CREATE TABLE websearch (id INTEGER IDENTITY PRIMARY KEY, url TEXT)""");

#Open file of URLs to put into database
file = open("urls.txt", "r")
for entry in file :
	cursor.execute("""INSERT INTO websearch (url) VALUES (?)""", entry.rstrip())
file.close()

for row in cursor.execute("SELECT * FROM websearch"):
	print(row);

connection.commit()
connection.close()
