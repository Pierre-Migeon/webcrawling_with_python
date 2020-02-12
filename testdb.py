import os
import pyodbc

connection = pyodbc.connect('DSN=pierres_sql_server;UID=sa;PWD=reallyStrongPwd123')
cursor = connection.cursor()

for row in cursor.execute("SELECT * FROM websearch"):
	print(row);

connection.close()
