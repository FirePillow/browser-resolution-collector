import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()
c = cursor.execute("SELECT * FROM data")
result = c.fetchall()
print(result)