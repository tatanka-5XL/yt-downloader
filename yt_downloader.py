from pytube import YouTube
from sys import argv
from datetime import datetime

link = argv[1]
yt = YouTube(link)
print(f'Video title is "{yt.title}"')

yd = yt.streams.get_highest_resolution()
print(f"It's size at highest resolution is {yd.filesize_mb} MB")

answer = input('Do you still want to download (y/n)?')
if answer.lower() == 'y':
    now = datetime.now()
    beginning = now.strftime("%H:%M:%S")
    print(f'Video download started at {beginning} - downloading...')
    yd.download('D:\Video\sb')
    now = datetime.now()
    end = now.strftime("%H:%M:%S")
    print(f'Video \"{yt.title}\" was downloaded sucessfully at {end}.')
else:
    print(f"Video \"{yt.title}\" wan't be downloaded.")
