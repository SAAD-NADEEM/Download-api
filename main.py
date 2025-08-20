from fastapi import FastAPI
from fastapi.responses import FileResponse
from mp3download import download_youtube_video

app = FastAPI(title="Download Youtube Videos", version="1.0.0")

@app.get("/")
def welcome():
    return {"message": "helooowww"}


@app.get("/download/{id}")
def get_vid(id):
    video_url = f"https://youtu.be/{id}"
    res = download_youtube_video(video_url)

    return FileResponse(
                path=f"downloads/{res.get("id")}.mp4",
                media_type='video/mp4',
                filename=f"{res.get("title")}.mp4"
            )