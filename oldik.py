import typer

import time
from frames.uzbekistan import piyola_frames
from frames.glass_frames import glass_frames
from frames.cheers_beers import beers_frames


DEFAULT_FRAMES = glass_frames

FRAMES = {
    "uzbekistan": piyola_frames,
    "cheers-beers": beers_frames,
}


def clear_line(n=1):
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    for i in range(n):
        print(LINE_UP, end=LINE_CLEAR)


def animate_cheers(keyword: str = ""):
    frames = FRAMES.get(keyword.lower(), DEFAULT_FRAMES)

    i = 0
    while True:
        line_count = len(frames)
        frame = frames[i]
        print(frame)
        time.sleep(.2)
        clear_line(len(frame.split("\n")))
        i += 1
        i %= line_count


def main(keyword: str = ""):
    animate_cheers(keyword)


if __name__ == '__main__':
    typer.run(main)
