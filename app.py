from flask import Flask, request, send_file
import downloader
import os
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
    if url != None:
        downloader.download(url)
    return data

@app.route("/file")
def file():
    dl = send_file('ytdlout.mp3', as_attachment=True, download_name="converted.mp3")
    return dl
