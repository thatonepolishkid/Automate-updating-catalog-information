#!/usr/bin/env python3
from PIL import Image
location = ''
def resize_and_rgb(image):
    im = Image.open(image)
    im = im.resize((600, 400))
    if im.mode != 'RGB':
        im.convert('RGB')
    im.save(location, 'JPEG', )