from pytube import YouTube

while True:
    url = input("Url: ")
    yt  = YouTube(url)
    streams = yt.streams
    for i in streams:
        if 'video' in i.mime_type:
            print(i.resolution)
        elif 'audio' in i.mime_type:
            print(i.abr)
