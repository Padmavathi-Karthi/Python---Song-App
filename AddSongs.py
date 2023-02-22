from ConnectSong import *
from ReadSongs import read
from time import sleep

"""

cursor.execute(
"""
# INSERT INTO songs VALUES(NULL, "Halamithi", "Anirudh", "Pop")

"""
)

connection.commit()

"""

# Exercise:

# To get the input from the user

def insertSongs():
    mySong = []
    title = input("Enter the song title: ")
    year = int(input("Enter the year of the song: "))
    artist = input("Enter an artist's name: ")
    genre = input("Enter the genre of the song: ")

    mySong.append(title)
    mySong.append(year)
    mySong.append(artist)
    mySong.append(genre)
    #print(mySong)
    cursor.execute(
    f"""
    INSERT INTO Music VALUES(NULL, "{mySong[0]}", "{mySong[1]}", "{mySong[2]}", "{mySong[3]}" )
    """
    )
    connection.commit()
    
    print(f"The song {title}, has been added successfully to the database.")
    sleep(3)
    read()

if __name__ == "__main__":  
    insertSongs()          # the function works only if we invoke or call the function

