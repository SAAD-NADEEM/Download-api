import yt_dlp
import os
from datetime import datetime


def download_youtube_video(video_url, save_path="downloads"):
    """
    Downloads a YouTube video with enhanced error handling and bypass techniques.

    Args:
        video_url (str): URL of the YouTube video.
        save_path (str): Directory to save the downloaded video.
    """
    try:
        # Create save directory if it doesn't exist
        os.makedirs(save_path, exist_ok=True)

        # Enhanced options for yt-dlp with bypass techniques
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": f"{save_path}/%(title)s.%(ext)s",
            "merge_output_format": "mp4",
            # Bypass techniques
            "extract_flat": False,
            "ignoreerrors": True,
            "quiet": False,
            "no_warnings": False,
            # Mimic a browser request
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Referer": "https://www.youtube.com/",
            },
            # Retry settings
            "retries": 10,
            "fragment_retries": 10,
            "skip_unavailable_fragments": True,
            # Throttle to avoid rate limiting
            "throttledratelimit": 1000000,
            # Cookies file if available (can help with age-restricted videos)
            "cookiefile": "cookies.txt" if os.path.exists("cookies.txt") else None,
            "extractor_args": {
                "youtube": {
                    "player_client": [
                        "android"
                    ],  # Pretend to be the YouTube Android app
                }
            },
        }

        print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting download...")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Additional debug info
            ydl.add_default_info_extractors()
            info_dict = ydl.extract_info(video_url, download=False)
            print(f"Downloading: {info_dict.get('title', 'Unknown Title')}")

            # Actual download
            ydl.download([video_url])
            return info_dict.get("title")

        print(
            f"[{datetime.now().strftime('%H:%M:%S')}] Video downloaded successfully to: {save_path}"
        )

    except yt_dlp.utils.DownloadError as e:
        print(f"Download Error: {e}")
        print("Possible solutions:")
        print("1. Try again later (YouTube might be blocking temporarily)")
        print("2. Update yt-dlp with: pip install --upgrade yt-dlp")
        print("3. Use a VPN if you're being IP blocked")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Consider reporting this issue to yt-dlp developers")