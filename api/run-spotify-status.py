from flask import Flask, Response, render_template
from base64 import b64encode
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

import requests, json, os, random

SPOTIFY_URL_REFRESH_TOKEN = "https://accounts.spotify.com/api/token"
SPOTIFY_URL_NOW_PLAYING = "https://api.spotify.com/v1/me/player/currently-playing"
SPOTIFY_URL_RECENTLY_PLAY = "https://api.spotify.com/v1/me/player/recently-played?limit=10"

SPOTIFY_CLIENT_ID = "70a153ec08c3465fa39e2f2b3ed6f19d"
SPOTIFY_SECRET_ID = "69375ea0a426477293cbfdef99dcbde0"
SPOTIFY_REFRESH_TOKEN = "AQDXZvg5_WVeraaPBQlyHfzsM2y1zekjGoi0UaDhhS18VcsyRFtvqQpZdUrNt7O0bdNrtO4waX3ZDHvCu9Dbz-xWSGA8RdSRsqV-k50__ouxpUntbTIiaxdFtwEe2l0BdxI"

BAR_COLOR = "#ff19c1"

app = Flask(__name__, template_folder="components")


def getAuth():
    return b64encode(f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_SECRET_ID}".encode()).decode("ascii")


def refreshToken():
    data = {
        "grant_type": "refresh_token",
        "refresh_token": SPOTIFY_REFRESH_TOKEN,
    }

    headers = {"Authorization": "Basic {}".format(getAuth())}

    response = requests.post(SPOTIFY_URL_REFRESH_TOKEN, data=data, headers=headers)
    return response.json()["access_token"]


def recentlyPlayed():
    token = refreshToken()
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(SPOTIFY_URL_RECENTLY_PLAY, headers=headers)

    if response.status_code == 204:
        return {}

    return response.json()


def nowPlaying():
    token = refreshToken()

    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(SPOTIFY_URL_NOW_PLAYING, headers=headers)

    if response.status_code == 204:
        return {}

    return response.json()


def soundVisualizer(soundBars):
    soundVisualizerCSS = ""
    START_BAR = 1700
    ANIMATIONS = ['animation1', 'animation2', 'animation3']
    for NTH in range(1, soundBars + 1):
        START_BAR += 100
        z = random.randint(0, 2)
        soundVisualizerCSS += ".spectrograph__bar:nth-child({0}) {{-webkit-animation-name: {1};animation-name: {1};" \
                              "-webkit-animation-duration: {2}ms;animation-duration: {3}ms;}}".format(NTH,
                                                                                                      ANIMATIONS[z],
                                                                                                      str(START_BAR),
                                                                                                      str(START_BAR))
    return soundVisualizerCSS


def loadImageB64(url):
    resposne = requests.get(url)
    return b64encode(resposne.content).decode("ascii")

def makeSVG(data):
    soundBars = 47
    soundVisualizerBar = "".join(["<div class='spectrograph__bar'></div>" for i in range(soundBars)])
    soundVisualizerCSS = soundVisualizer(soundBars)

    if data == {}:
        recent_plays = recentlyPlayed()
        size_recent_play = len(recent_plays["items"])
        idx = random.randint(0, size_recent_play - 1)
        item = recent_plays["items"][idx]["track"]
    else:
        item = data["item"]
    albumCover = loadImageB64(item["album"]["images"][1]["url"])
    artistName = item["artists"][0]["name"].replace("&", "&amp;")
    songName = item["name"].replace("&", "&amp;")

    spotifyObject = {
        "soundVisualizerBar": soundVisualizerBar,
        "soundVisualizerCSS": soundVisualizerCSS,
        "artistName": artistName,
        "songName": songName,
        "albumCover": albumCover,
        "barColor": BAR_COLOR
    }

    return render_template("spotifyStatus.html.j2", **spotifyObject)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    data = nowPlaying()
    svg = makeSVG(data)

    resp = Response(svg, mimetype="image/svg+xml")
    resp.headers["Cache-Control"] = "s-maxage=1"

    return resp


if __name__ == "__main__":
    app.run(debug=True)
