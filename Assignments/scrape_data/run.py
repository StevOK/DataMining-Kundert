# Steven Kundert
# CMPS 5443 Data Mining - Griffin
# Assignment 2 - Scraping Data
# 9/18/17
# This program will go to Rolling Stone's list of the 500 Greatest Songs of All Time
# and scrape the number, artist, and song title for the top 100 songs. Since 
# each song has its own node, my code must find the link to the next node in the
# list and go from there.

import requests
from bs4 import BeautifulSoup
import time
import random
import operator
import csv

# Create a list to hold all the songs
song_list = []

# Base url for the list, must find the next node before scraping
# Start at the 101st song
url = "http://www.rollingstone.com/music/lists/the-500-greatest-songs-of-all-time-20110407/the-rolling-stones-you-cant-always-get-what-you-want-20110526"

# Load up the code from the current node and turn into soup
html = requests.get(url).text
soup = BeautifulSoup(html,'html.parser')

# Go to the songs 100 to 1
for i in range(100):    
    # Locate and go to the next node in the list
    url = 'http://www.rollingstone.com' + soup.find(attrs={'class':'pagination-collection load-more'}).get('href')
    
    # Now load the new page into a soup object
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    
    # Grab the line with the pertinent information
    infoline = soup.find(attrs={'id':'collection-items-container'}).findNext('h2')
    # Convert to a string without tags
    info = infoline.text
    
    # Find the song number
    numend = info.find('.')
    num = info[:numend]
    
    # Find the artist
    artistend = info.find(',')
    artist = info[numend+2:artistend]
    
    # Find the song title
    song = info[artistend+2:]
    
    # Create a dictionary to hold each track's info
    song_dict = {}
    
    # Stuff the info into the dictionary
    song_dict['number'] = int(num.strip()) # Needs to be int for sorting
    song_dict['artist'] = artist.strip()
    song_dict['song'] = song.strip()
    
    # Append the dictionary to the list
    song_list.append(song_dict)
    
    # Pause a bit so as not to be mistaken for someone doing an attack
    time.sleep(random.randint(0,3))
           
# Sort the list by number so that #1 is at the top of the list    
song_list.sort(key=operator.itemgetter('number'))

# Open a csv file,
# Make the fieldnames line up with the keys of the dictionaries
# Write the header, then write the rest of the table
with open('top100songs.csv', 'w') as myfile:
    keys = ['number','artist','song']
    wr = csv.DictWriter(myfile, keys)
    wr.writeheader()
    wr.writerows(song_list)
