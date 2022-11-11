import typer

import time
from frames import glass_frames, piyola_frames, beer_frames

DEFAULT_FRAMES = glass_frames

COUNTRY_TO_FRAMES = {
    "uzbekistan": piyola_frames,
    "germany": beer_frames
}


def clear_line(n=1):
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    for i in range(n):
        print(LINE_UP, end=LINE_CLEAR)


def animate_cheers(country: str = ""):
    frames = COUNTRY_TO_FRAMES.get(country.lower(), DEFAULT_FRAMES)

    i = 0
    while True:
        line_count = len(frames)
        frame = frames[i]
        print(frame)
        time.sleep(.2)
        clear_line(len(frame.split("\n")))
        i += 1
        i %= line_count


def main(country: str = ""):
    animate_cheers(country)


if __name__ == '__main__':
    typer.run(main)
