import sys 
import os
import spotifyData as spotify
from youtubeDownload import musicDownloader
import config

artistInfo = spotify.getArtistInfo()
videoIds = spotify.getVideoIds(artist=artistInfo)

videoIds = config.VIDEO_IDS


#filePath = config.FILE_PATH %('LANY', 'Malibu Nights')
filePath = config.FILE_PATH %(artistInfo[0], videoIds[1])

musicDownloader(filePath=filePath, videoIdList=videoIds[0])
#musicDownloader(filePath=filePath, videoIdList=videoIds)