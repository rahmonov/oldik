
<h1 align="center">
  <br>
  <a href="https://t.me/jakhonrakhmonov"><img src="https://raw.githubusercontent.com/rahmonov/oldik/main/images/clinking-glasses.png" alt="Oldik" width="200"></a>
  <br>
  Oldik
  <br>
</h1>

<h4 align="center">A small fun project to give tribute to the <a href="https://t.me/jakhonrakhmonov/32">"Oldik 🥂" meme</a>.</h4>

![screenshot](https://raw.githubusercontent.com/rahmonov/oldik/main/images/oldik.gif)

## To Contribute

1. Add your frames to `frames.py`. You can use https://www.text-image.com/convert/ascii.html to convert images to frames.
1. Import it from the `frames/__init__.py`
1. Import it from `oldik.py`.
1. Add your imported frame to the `VERSION_TO_FRAMES` dictionary. It has to map to a version name. For example, Uzbekistan maps to piyola frames..
1. That's it.

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/rahmonov/oldik.git

# Go into the repository
$ cd oldik

# Install dependencies
$ pip install -r requirements.txt

# Run the app
$ python oldik.py

# Try other options
$ python oldik.py --version=uzbekistan
```
