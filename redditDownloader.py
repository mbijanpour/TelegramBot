import os
from redvid import Downloader



def download(link: str) -> str:
    """
    download the reddit video with the link passed to the argument and it will return the path of the
    downloaded video to bot.py
    """
    # Add the FFmpeg directory to the system's PATH environment variable
    ffmpeg_directory = "C:/ffmpeg-2023-06-26-git-285c7f6f6b-essentials_build/bin"
    os.environ['PATH'] += os.pathsep + ffmpeg_directory
    reddit = Downloader(min_q=True)
    reddit.url = link
    reddit.path = 'D:/random py/reddit/vids'
    print(os.path.basename(reddit.file_name))
    video_path = reddit.download()
    print(reddit.file_name)
    # print(f"path:{video_path}")
    return video_path
