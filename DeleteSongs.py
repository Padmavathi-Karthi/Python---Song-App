from ConnectSong import *
from ReadSongs import read
from time import sleep

# Delete FROM songs WHERE SongID = "id"
"""
read()
givenID = input("\nEnter the ID of the song you would like to delete: ")

#print("Deleting song of ID:", givenID)

cursor.execute(f"DELETE FROM songs WHERE SongID = {givenID}")

connection.commit()

print(f"The Song of ID {givenID} has been deleted.")

sleep(2)

read()

"""

# Another Way for Deleting - while loop validation

def delete():
    read()

    sure = False

    while sure == False:
        givenID1 = input("\nEnter the ID of the song you would like to delete: ")
        print(f"You have selected song of ID {givenID1}. ")
        confirm = input(f"Is this correct? y/n ")
        if confirm == "y":
            sure = True

    cursor.execute(f"DELETE FROM Music WHERE SongID = {givenID1}")
    connection.commit()

    print(f"The Song of ID {givenID1} has been deleted.")
    sleep(2)
    read()

if __name__ == "__main__":
    delete()

