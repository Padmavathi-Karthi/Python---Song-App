import sqlite3 as sql

# connect(filepath to database)
connection = sql.connect(r"C:\Users\padhu\Desktop\JustIT\Python\Final Song Database Project\Music.db")

cursor = connection.cursor()
