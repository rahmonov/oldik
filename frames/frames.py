from PIL import Image
from pathlib import Path


def get_ascii_frames(file_path):
    """
    Open and convert file to ascii art
    """
    path = Path(file_path)
    frames = []

    with Image.open(path) as img:
        total_frames = img.n_frames
        for i in range(total_frames):
            img.seek(i)
            img.save(f"images/frames/{i}.png")

    for i in range(total_frames):
        with Image.open(f"images/frames/{i}.png") as img:
            width, height = img.size
            aspect_ratio = height / width
            new_width = 100
            new_height = aspect_ratio * new_width * 0.55
            img = img.resize((new_width, int(new_height)))
            img = img.convert('L')

            pixels = img.getdata()

            chars = ['#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']

            new_pixels = [chars[pixel // 25] for pixel in pixels]
            new_pixels = "".join(new_pixels)

            new_pixels_count = len(new_pixels)
            ascii_image = [new_pixels[index: index + new_width] for index in range(0, new_pixels_count, new_width)]
            ascii_image = "\n".join(ascii_image)

            frames.append(ascii_image)

    return frames
