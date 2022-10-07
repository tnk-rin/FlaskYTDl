from flask import Flask, request, send_file
import downloader
import os
import io
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    with open('index.html', 'r') as file:
        data = file.read()
    return data

@app.route("/download")
def download():
    with open('index.html', 'r') as file:
        data = file.read()
    url = request.args.get('url')
    mode = request.args.get('mode')
    if url != None:
        downloader.download(url, mode)
    return data

@app.route("/file")
def file():
    mode = request.args.get('mode')
    filename = "tmp/ytdlout.mp3" if mode == 'audio' else "tmp/ytdlout.mp4"
    mime = "audio/mpeg" if mode == 'audio' else "video/mp4"
    path = os.path.join(os.getcwd(), filename)

    return_data = io.BytesIO()
    with open(path, 'rb') as fo:
        return_data.write(fo.read())
    return_data.seek(0)

    os.remove(path)

    r = send_file(return_data, mimetype=mime, as_attachment=True, attachment_filename="converted.mp3")
    return r


def filer():
    mode = request.args.get('mode')
    filename = "tmp/ytdlout.mp3" if mode == 'audio' else "tmp/ytdlout.mp4"
    dl = send_file(filename, as_attachment=True, download_name="converted.mp3")
    return dl
