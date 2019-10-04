from __future__ import unicode_literals
import youtube_dl


def musicDownloader(filePath):
    ydl_opt = {
        'format': 'bestaudio/best',
        'postprocessor': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }