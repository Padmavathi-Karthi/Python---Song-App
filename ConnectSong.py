import sqlite3 as sql

# connect(filepath to database)
connection = sql.connect(r"C:\Users\padhu\Desktop\GitHub\Python---Song-App\Music.db")

cursor = connection.cursor()
