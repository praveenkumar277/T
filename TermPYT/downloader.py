import curses
import printer
import av
import playlistav

class Downloader():
    def __init__(self, playlist: list[list], Window = curses.initscr()) -> None:
        self.window = Window
        self.__plist = playlist
        self.__loadDownloader()

    def __loadDownloader(self) -> None:
        self.__maxy, self.__maxx = self.window.getmaxyx()

    def __downloader(self) -> None:
        for i, plist in enumerate(self.__plist):
            ...

    def __call__(self) -> None:
        pass

if __name__ == '__main__':
    c = curses.initscr() 
    c.keypad(True)
    curses.mousemask(curses.ALL_MOUSE_EVENTS)
    curses.noecho()
    curses.curs_set(0)
    d = [{'res': 480, 'type': 'video', 'mime': 'mp4/webm', 'stream': 'adaptive', 'size': '--/--'},
    {'abr': 50, 'type': 'audio', 'mime': 'mp4/webm', 'stream': 'adaptive', 'size': '--/--'}]
    #b = av.AV('https://youtu.be/XnJt8WYxZ0o?si=ALOOPh0CT3kM2tQ8',c)
    #b = playlistav.PlaylistAV('https://youtube.com/playlist?list=PLLVAlrhlWEFzGpmql5-FJrWQ5dIGO14HT&si=SHfpjQ7IntNX8nfl', [{'abr': 70, 'type': 'audio', 'mime': 'mp4/webm', 'stream': 'adaptive', 'size': '--/--'}], c)
    b = playlistav.PlaylistAV('https://youtube.com/playlist?list=PLLVAlrhlWEFzGpmql5-FJrWQ5dIGO14HT&si=SHfpjQ7IntNX8nfl', d, c)

    try:
        a= 0
    except Exception as e:
        curses.endwin()
        print(e)
    else:
        curses.endwin()
        print(a) 

