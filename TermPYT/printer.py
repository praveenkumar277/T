from functools import reduce
from pytube import Stream, StreamQuery

def formatter1(strings: list[str], width: int) -> list[str]:
    line1: str = strings[0] [:width] + chr(32) * (width - len(strings[0] [:width]))
    extra: str = chr(32) + strings[1] + chr(32) + strings[2]

    if len(strings[0] [width:]) > (width - len(extra)):
        line2: str = strings[0] [width:] [:(width - len(extra))] [:-8] + chr(46) * 3 +strings[0] [-5:]
    else:
        line2: str = strings[0] [width:] + (chr(32) * (width - len(extra) - len(strings[0] [width: ])))

    return [line1, line2, extra]

def formatter2(strings: list[list[str]], width: int) -> list[list[list[str]]]:
    """
    Input:    ["Res/Abr", "Audio/Video", "mp4/webm", "Progressive/Adaptive", "Size"]
    Output:
        [[" Res/Abr   ", "Audio/Video  ", "mp4/webm"],
        ["Progressive/Adaptive", "Size"]]
    """
    ww = int(width/ 3)
    formated_list: list = list()
    for i in strings:
        list1 = [(i[0] + (chr(32) * (ww - len(i[0])))), (i[1] + ( chr(32) * (ww - len(i[1])))), (i[2] + ( chr(32) * (ww - len(i[2]))))]
        list2 = [(i[3] + chr(32) * (width - len(i[4]) - len(i[3]))), (i[4])]
        formated_list.append([list1, list2])

    return formated_list

class Box():
    def __init__(self, x_pos: int, y_pos: int, width: int, lines: int, Window, style: int = 0) -> None:
        self.__x_pos    = x_pos
        self.__y_pos    = y_pos
        self.__width    = width
        self.__line     = lines
        self.__style    = style
        self.window     = Window
    
    def __box(self, i: int, style: int = 0) -> None:
        style = self.__style if style == 0 else style
        self.window.addstr(self.__y_pos + ( i * (self.__line + 2) ), self.__x_pos,chr(9581) + chr(9472) * self.__width + chr(9582), style)
        self.window.addstr(self.__y_pos + ( i * (self.__line + 2) ) + self.__line + 1, self.__x_pos,chr(9584) + chr(9472) * self.__width + chr(9583), style)
        for j in range(self.__line):
            self.window.addstr(self.__y_pos + ( i * (self.__line + 2) ) + j +1, self.__x_pos, chr(9474), style)
            self.window.addstr(self.__y_pos + ( i * (self.__line + 2) ) + j +1, self.__x_pos + 1 + self.__width, chr(9474), style)

    def boxes(self, quantity: int):
        for i in range(quantity):
            self.__box(i)

    def editStyle(self, n: int, style: int):
        self.__box(n, style)

def printer1(data: list[str], y: int, c_pos: int,style: tuple[int, int], window) -> None:
    window.addstr(y, c_pos, data[0], style[0])
    window.addstr(y +1, c_pos, data[1], style[0])
    window.addstr(y +1, c_pos + len(data[1]), data[2], style[1])
    window.refresh()

    
def printer2(data: list[list[str]], y: int, c_pos: int, style: dict, window) -> None:
    window.addstr(y + 1,   c_pos , data[0][0], style["res"])
    window.addstr(y + 1,   c_pos + len(data[0][0]), data[0][1], style["type"])
    window.addstr(y + 1,   c_pos + len(data [0][0] + data[0][1]), data[0][2], style["mime"])
    window.addstr(y + 2,   c_pos , data[1][0], style["prog"])
    window.addstr(y + 2,   c_pos + len(data[1][0]), data[1][1], style["size"])

def filter(stream_str: list, stream) -> tuple:
    rstream: list = [None, None]
    for i in stream.filter(type='video').filter(file_extension='mp4'):
        if stream_str[0] is None:
            rstream[0] = None
            break

        if i.is_progressive:
            continue

        if int(i.resolution[:-1]) == stream_str[0]:
            rstream[0] = i
            break
    else:
        for i in stream.filter(type='video'):
            if int(i.resolution[:-1]) == 360 and not i.is_progressive:
                rstream[0] = i
                stream_str[0] = 360
                break
    
    for i in stream.filter(type='audio'):
        if int(i.abr[:-4]) == stream_str[1]:
            rstream[1] = i
            break
    else:
        rstream[1] = stream.filter(type='audio').first()
        stream_str[1] = int(stream.filter(type='audio').first().abr[:-4])

    return (stream_str, rstream)

def formatter3(stream: StreamQuery, type: str) -> list:
    lStream: Stream = reduce(lambda x, y: x if len((x.resolution if type == 'video' else x.abr) + str(round(x.filesize_mb, 1))) > len((y.resolution if type == 'video' else y.abr) + str(round(y.filesize_mb, 1))) else y, stream)
    strlen: int = len((lStream.resolution if type == 'video' else lStream.abr) + str(round(lStream.filesize_mb, 1))) + 1
    options: list = list(map(lambda x: (x.resolution if type == 'video' else x.abr) + chr(32) * (strlen - len((x.resolution if type == 'video' else x.abr) + str(round(x.filesize_mb, 1)))) + str(round(x.filesize_mb, 1)) + 'M', stream))
    return options

