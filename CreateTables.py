from ConnectSong import *

"""
MULTI - LINE STRING

"""

cursor.execute(

"""
CREATE TABLE "Music"(
    "SongID"    INTEGER NOT NULL UNIQUE,
    "Title"     TEXT,
    "Year"      INTEGER,
    "Artist"    TEXT,
    "Genre"     TEXT,
    PRIMARY KEY("SongID" AUTOINCREMENT)

)

"""
)
