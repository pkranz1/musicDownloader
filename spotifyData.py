import os
import sys
import json
import spotipy
import webbrowser
from spotipy.oauth2 import SpotifyClientCredentials
from json.decoder import JSONDecodeError
import config
import argparse
from youtubeData import youtubeSearch

client_credentials_manager = SpotifyClientCredentials(
    client_id = config.Cridentials.CLIENT_ID,
    client_secret = config.Cridentials.CLIENT_SECRET
)

#token authorization
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

albumDictonary = {}
trackList = [] 
albumNames = []
videoIds = []

#user inputs artists name
artist = input('Artist: ')

#artist search to obtain artist id
artist = sp.search(q=artist, limit=5, type='artist')
artistId = artist['artists']['items'][0]['id']
artist = artist['artists']['items'][0]['name']

#gets albums by artist 
albums = sp.artist_albums(artist_id=artistId, limit=30)
count = 0
#dictonary where the key is the album name and the value is the album id.
for album in albums['items']:
    albumDictonary[album['name']] = album['id']
    albumNames.append(album['name'])

for key in albumDictonary.keys():
    print(key)

while True:
    try:
        album = input('Please copy and paste Album title from above: ')
        tracks = sp.album_tracks(albumDictonary[album])
        break
    except KeyError:
        album = input('Error: Please copy and paste Album title from above: ')
        pass

count = 0

for track in tracks['items']:
    trackList.append(track['name'])
    try:
        videoIds.append(youtubeSearch(artist,trackList[count]))
    except(HttpError, error):
        print('Http Error: %d occured:\n\t%s' % (error.resp.status, error.content))
    count += 1












