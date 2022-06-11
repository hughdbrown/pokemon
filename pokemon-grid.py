#!/usr/bin/env python3

from pathlib import Path

from PIL import Image, ImageChops

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

def new_file(filename, width, height):
    x_n, y_n = 3, 3
    x_margin, y_margin = 10, 10
    x_space, y_space = 6, 6
    x_extent = x_n * width + (x_n - 1) * x_space + 2 * x_margin
    y_extent = y_n * height + (y_n - 1) * y_space + 2 * y_margin
    new_im = Image.new('RGB', (x_extent, y_extent))
    im = Image.open(filename)

    trimmed = trim(im)
    if trimmed:
        im = trimmed
    im = im.resize((width, height))

    for i in range(x_n):
        x = x_margin + i * (width + x_space)
        for j in range(y_n):
            y = y_margin + j * (height + y_space)
            new_im.paste(im, (x, y))

    p = Path(filename)
    newfilename = Path(p.stem + "-grid").with_suffix(".png")
    new_im.save(newfilename)
    print(f'Saving {newfilename}')

# -rw-r--r--@ 1 hughbrown  staff  33499 Aug 11 17:09 daddy-pokemon-card.jpeg
# -rw-r--r--@ 1 hughbrown  staff  42163 Aug 11 17:36 tyler-gx-pokemon.jpeg
# width = 373
# height = 521

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            for path in Path.cwd().glob(arg):
                new_file(path, 373, 521)
    else:
        #new_file('daddy-pokemon-card.jpeg', 373, 521)
        #new_file('tyler-gx-pokemon.jpeg', 373, 521)
        #new_file('connor-gx.jpeg', 373, 521)
        #new_file('arceus-gx-pokemon.jpeg', 373, 521)
        new_file('plane-pokemon.jpeg', 373, 521)
        new_file('MagikarpWailordGXSMPromo166.jpeg', 373, 521)


