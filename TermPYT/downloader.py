import curses

class Downloader():
    def __init__(self) -> None:
        pass

    def download(self) -> None:
        pass
if __name__ == '__main__':
    c = curses.initscr() 
    c.keypad(True)
    curses.mousemask(curses.ALL_MOUSE_EVENTS)
    curses.noecho()
    curses.curs_set(0)
    #b = AV('https://youtu.be/CzSL-YKjYn4?si=R00q1KYp7egDfimwH0',c)
    a= None
    curses.endwin()
    print(a) 

