from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json
import re

api_key = 'AIzaSyAfE37oNX_dgdcXpxFhc7mU_MnviLJA4kU'

def youtubeSearch(artist, track):
    youtube = build(serviceName='youtube',version='v3',developerKey=api_key,)

    search_response = youtube.search().list(
        q=track + ' by ' + artist,
        part= 'snippet',
        type='video'
    ).execute()

    #print(json.dumps(obj=search_response, sort_keys=True, indent=2))

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
    return(videoIds)
            
            




