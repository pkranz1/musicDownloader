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

#allows use of the spotify api
client_credentials_manager = SpotifyClientCredentials(
    client_id = config.Cridentials.CLIENT_ID,
    client_secret = config.Cridentials.CLIENT_SECRET
  )

#token authorization
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#returns a list containing the artists name as the first element
#and the artistID as the second element
def getArtistInfo():
  #user inputs artists name
  artist = 'LANY' #input('Artist: ')

  #artist search to obtain artist id
  artist = sp.search(q=artist, limit=5, type='artist')
  artistId = artist['artists']['items'][0]['id']
  artist = artist['artists']['items'][0]['name']

  #returns artist information
  return [artist, artistId]

#retuns a list containing all relevant videoIds pulled from youtube
#arguement is intended to be the list returned by the getArtstInfo
#function
def getVideoIds(artist):
  albumDictonary = {}
  trackList = [] 
  albumNames = []
  videoIds = []
  
  #gets albums by artist 
  albums = sp.artist_albums(artist_id=artist[1], limit=30)
  count = 0
  
  #dictonary where the key is the album name and the value is the album id.
  for album in albums['items']:
    albumDictonary[album['name']] = album['id']
    albumNames.append(album['name'])

  for key in albumDictonary.keys():
    print(key)

  #user inputs album of choice
  while True:
    try:
      album = 'Malibu Nights' #input('Please copy and paste Album title from above: ')
      tracks = sp.album_tracks(albumDictonary[album])
      break
    except KeyError:
      album = input('Error: Please copy and paste Album title from above: ')
      pass
  
  count = 0

  for track in tracks['items']:
    trackList.append(track['name'])
    videoIds.append(youtubeSearch(artist[0],trackList[count]))
    count += 1
  
  return videoIds













