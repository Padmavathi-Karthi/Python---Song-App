from ConnectSong import *

def read():
    cursor.execute("SELECT * FROM Music1")
    rows = cursor.fetchall()

    # print (rows)            # it will return the result in "List"
    # print (type(rows))
    print("\nSong List: ")
    for record in rows:
        # print(type(record))
        print(record)             # it will return the result in "Tuple"

if __name__ == " __main__":       # it stops to run the read() function automatically.
    read()
