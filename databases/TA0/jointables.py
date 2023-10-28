# You do not need to export or convert the database - simply upload the .sqlite file that your program creates. See the example code for the use of the connect() statement.
#
# Musical Track Database
# This application will read an iTunes export file in XML and produce a properly normalized database with this structure:
#
# CREATE TABLE Artist (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
# name    TEXT UNIQUE
# );
#
# CREATE TABLE Genre (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
# name    TEXT UNIQUE
# );
#
# CREATE TABLE Album (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
# artist_id  INTEGER,
# title   TEXT UNIQUE
# );
#
# CREATE TABLE Track (
#     id  INTEGER NOT NULL PRIMARY KEY
# AUTOINCREMENT UNIQUE,
# title TEXT  UNIQUE,
# album_id  INTEGER,
# genre_id  INTEGER,
# len INTEGER, rating INTEGER, count INTEGER
# );
# If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.
#
# You can use this code as a starting point for your application: http://www.py4e.com/code3/tracks.zip. The ZIP file contains the Library.xml file to be used for this assignment. You can export your own tracks from iTunes and create a database, but for the database that you turn in for this assignment, only use the Library.xml data that is provided.
#
# To grade this assignment, the program will run a query like this on your uploaded database and look for the data it expects to see:
#
# SELECT Track.title, Artist.name, Album.title, Genre.name
# FROM Track JOIN Genre JOIN Album JOIN Artist
# ON Track.genre_id = Genre.ID and Track.album_id = Album.id
# AND Album.artist_id = Artist.id
# ORDER BY Artist.name LIMIT 3
# The expected result of the modified query on your database is: (shown here as a simple HTML table with titles)
# Track	Artist	Album	Genre
# Chase the Ace	AC/DC	Who Made Who	Rock
# D.T.	AC/DC	Who Made Who	Rock
# For Those About To Rock (We Salute You)	AC/DC	Who Made Who	Rock
#
# In[ ]:
#
import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
# cur.executescript('''
# DROP TABLE IF EXISTS Artist;
# DROP TABLE IF EXISTS Album;
# DROP TABLE IF EXISTS Track;
# DROP TABLE IF EXISTS Genre;
#
# CREATE TABLE Artist (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );
#
# CREATE TABLE Genre (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );
#
# CREATE TABLE Album (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     artist_id  INTEGER,
#     title   TEXT UNIQUE
# );
#
# CREATE TABLE Track (
#     id  INTEGER NOT NULL PRIMARY KEY
# AUTOINCREMENT UNIQUE,
#     title TEXT  UNIQUE,
#     album_id  INTEGER,
#     genre_id  INTEGER,
#     len INTEGER, rating INTEGER, count INTEGER
# );
# ''')

# fname = input('Enter file name: ')
fname = 'Library.xml'
if (len(fname) < 1):
    fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
# <key>Composer</key><string>John Deacon</string>
# <key>Album</key><string>Greatest Hits</string>
# <key>Genre</key><string>Rock</string>
# <key>Kind</key><string>MPEG audio file</string>
# <key>Size</key><integer>4344295</integer>
# <key>Total Time</key><integer>217103</integer>
# <key>Disc Number</key><integer>1</integer>
# <key>Disc Count</key><integer>1</integer>
# <key>Track Number</key><integer>3</integer>
# <key>Track Count</key><integer>17</integer>
# <key>Year</key><integer>1980</integer>
# <key>Date Modified</key><date>2006-02-14T16:13:02Z</date>
# <key>Date Added</key><date>2006-02-14T16:13:02Z</date>
# <key>Bit Rate</key><integer>160</integer>
# <key>Sample Rate</key><integer>44100</integer>
# <key>Comments</key><string></string>
# <key>Play Count</key><integer>55</integer>
# <key>Play Date</key><integer>3518868192</integer>
# <key>Play Date UTC</key><date>2011-03-29T16:43:12Z</date>
# <key>Rating</key><integer>100</integer>
# <key>Album Rating</key><integer>100</integer>










