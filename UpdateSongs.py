from ConnectSong import *
from ReadSongs import read
from time import sleep

def update():
    # Taken the ID
    givenID = input("Enter the ID of the song you'd like to update: ")

    title = input("Enter the new title: ")
    year = int(input("Enter the new year of the song: "))
    artist = input("Enter the new artist: ")
    genre = input("Enter the new genre: ")

# Update SQL Statement

    cursor.execute(
    f"""
    UPDATE Music
    SET Title = "{title}", Year = "{year}", Artist = "{artist}", Genre = "{genre}"
    WHERE SongID = {givenID}
    ;
    """
    )
    connection.commit()

    print(f"Song ID {givenID} has been successfully updated. ")

    sleep(2)
    read()

if __name__ == "__main__":
    update()

