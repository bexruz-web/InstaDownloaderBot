import requests

from config import X_RAPIADI_KEY, X_RAPIADI_HOST, API_URL


def video_downloader(video_url: str):
    url = API_URL

    querystring = {"url": video_url}

    headers = {
        "x-rapidapi-key": X_RAPIADI_KEY,
        "x-rapidapi-host": X_RAPIADI_HOST
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()
