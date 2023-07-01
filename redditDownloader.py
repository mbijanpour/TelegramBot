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

    # the process of getting the links downloading the video with redvid library
    # link to the github repo: https://github.com/elmoiv/redvid
    # the restrictions of the internet couldn't fit the max_q yet
    reddit = Downloader(min_q=True) 
    reddit.url = link
    reddit.path = 'D:/random py/reddit/vids' # path to the file for saving the videos
    video_path = reddit.download()
    
    return video_path # the video_path is the path of the downloaded file
