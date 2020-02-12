
import os
import pyodbc

connection = pyodbc.connect('DSN=pierres_sql_server;UID=sa;PWD=reallyStrongPwd123')
cursor = connection.cursor()

cursor.execute("""IF object_id('websearch', 'U') is null CREATE TABLE websearch (id INTEGER PRIMARY KEY, url TEXT)""");

file = open("urls.txt", "r")
for entry in file :
	cursor.execute("""INSERT INTO websearch (url) VALUES ({?})""", entry);

connection.commit()
connection.close()
