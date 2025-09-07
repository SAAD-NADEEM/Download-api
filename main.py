from fastapi import FastAPI
from fastapi.responses import FileResponse
from mp3download import download_youtube_video


app = FastAPI(title="Download Youtube Videos", version="1.0.0")


@app.get("/")
def welcome():
    return {"message": "helooowww"}


@app.get("/download/")
def get_vid(id: str):
    video_url = f"https://youtu.be/{id}"
    res = download_youtube_video(video_url)
    return {"message": res}