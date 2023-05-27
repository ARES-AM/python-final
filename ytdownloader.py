from pytube import YouTube
from sys import argv
link = argv[1]
yt=YouTube(link)
ytd=yt.streams.get_highest_resolution()
ytd.download('/home/ares_am/Desktop/ytdownload')
