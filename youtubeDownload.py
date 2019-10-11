from __future__ import unicode_literals
import youtube_dl


def musicDownloader(filePath, videoIdList):
  ydl_opt = {
    'format': 'bestaudio/best',
    'postprocessor': [{
    'key': 'FFmpegExtractAudio',
    'preferredcodec': 'mp3',
    'preferredquality': '192',
    }],
    'outtmpl':filePath+'%(title)s.%(ext)s',
    }

  for idList in range(0,len(videoIdList)):
    with youtube_dl.YoutubeDL(ydl_opt) as ydl:
      print(ydl)
      print('\n')
      ydl.download(['https://www.youtube.com/watch?v='+ str(videoIdList[idList][0])])
  
  print('\nDownload completed')