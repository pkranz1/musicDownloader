from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from config import Youtube
import re

youtube = build(serviceName='youtube',version='v3',developerKey=Youtube.API_KEY,)

def youtubeSearch(artist, track):
  search_response = youtube.search().list(
    q=track + ' by ' + artist,
    part= 'snippet',
    type='video',
    maxResults=3
  ).execute()

  videoIds = []
  misc = []
  count = 0
    
  for result in search_response.get('items', []):
    try:
      kind = result['id']['kind']
      title = result['snippet']['title']
            
    except KeyError:
      pass
        
    else:
      if kind == 'youtube#video' and re.search(pattern=artist, string=title, flags=re.IGNORECASE):
        videoId = result['id']['videoId']
        videoIds.append(videoId)
      else:
        misc.append(kind)
        count += 1
  
  return videoIds
            
            




