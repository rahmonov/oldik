import typer
import time
from frames import piyola_frames, beer_frames, glass_frames, cola_frames, broken_glass_frames,wine_frames,get_ascii_frames

DEFAULT_FRAMES = glass_frames

VERSION_TO_FRAMES = {
    "uzbekistan": piyola_frames,
    "germany": beer_frames,
    "canada": broken_glass_frames,
    "cola": cola_frames,
    "italy": wine_frames,
}


def clear_line(n=1):
    LINE_UP = "\033[1A"
    LINE_CLEAR = "\x1b[2K"
    for i in range(n):
        print(LINE_UP, end=LINE_CLEAR)


def animate_frames(frames):
    i = 0
    while True:
        # validate frames length
        if len(frames) == 0:
            return
        line_count = len(frames)
        frame = frames[i]
        print(frame)
        time.sleep(0.2)
        clear_line(len(frame.split("\n")))
        i += 1
        i %= line_count


def animate_version(version: str = ""):
    frames = VERSION_TO_FRAMES.get(version.lower(), DEFAULT_FRAMES)
    animate_frames(frames)

# animate_gif converts gif file to frames and animates as ascii art
def animate_gif(path: str):
    frames = get_ascii_frames(path)
    animate_frames(frames)

def main(version: str = "uzbekistan", path: str = None):
    # If gif path specified, then animate gif
    if path:
        animate_gif(path)
        return
    animate_version(version)


if __name__ == '__main__':
    typer.run(main)
