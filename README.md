# Purpose
Python scripts to scale graphics and pave them within a grid. Useful for making Pokemon-like cards with 5:7 aspect ratio.

# Programs
1. pokemon-grid.py  
The original. Puts JPEG into a 3x3 grid and produces a PNG file. The resulting file, when printed, can be easily cut into 9 cards.
2. pokemon-grid-horizontal.py  
A quick modification to deal with images that have an aspect ratio that is too wide.
3. openai-pokemon-grid.py  
An interactive program created by OpenAI from a prompt. In theory, this makes it easier to iterate on code changes.


# OpenAI prompt to create program
```
Write python code for an interactive program to edit graphics. Recommend using PIL library.
The program has a limited set of operations:
- open file (as JPG/JPEG)
- save file (as PNG)
- scale the image to a box (with x- and y-dimensions)
- define a grid (typically 3 by 3) that the image is written into, so that a single piece of paper has multiple images
The boxes in the grid should have narrow black lines drawn around their extent.
- rotate the image
- change the image's size within each grid box
```
