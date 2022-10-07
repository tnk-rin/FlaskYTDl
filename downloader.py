from __future__ import unicode_literals
import yt_dlp

def download(url, mode):
    ydl_opts = {}
    if mode == "audio":
        ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': 'tmp/ytdlout.%(ext)s',
            }
    elif mode == "video":
        ydl_opts = {
                'format': 'mp4+ba/b',
                'outtmpl': 'tmp/ytdlout.%(ext)s',
                }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    print("This cannot be run as a standalone applet")
    exit()
