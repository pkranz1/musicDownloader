import sys 
import os
import spotifyData as spotify
import config

artistInfo = spotify.getArtistInfo()
videoIds = spotify.getVideoIds(artist=artistInfo)
print(videoIds)