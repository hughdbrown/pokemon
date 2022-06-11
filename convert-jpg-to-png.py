#!/usr/bin/env python3

from pathlib import Path
from sys import argv

from PIL import Image

def main(jpg_name: Path, png_name: Path):
    print(f'{jpg_name}')
    print(f'{png_name}')
    if not jpg_name.exists() and jpg_name.isfile():
        logger.error(f"{jpg_name} does not exist")
    else:
        image = Image.open(str(jpg_name)
        image.save(str(png_name))


if __name__ == '__main__':
    args = argv[1:]
    for arg in args:
        jpg_name = Path(arg).expanduser()
        png_name = jpg_name.with_suffix('.png')
        main(jpg_name, png_name)

