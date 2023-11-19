#!/usr/bin/env python3
import os
from PIL import Image

folder_dir = r'C:\Users\<INSERT USER HERE>\Desktop\phone_pictures'
destination_dir = r'C:\Users\<INSERT USER HERE>\Desktop\move pictures to folder\\'

def rename_img(folder):
    '''If OSError has been raised, this means that the file which is trying to be converted is unable to do so.'''
    for infile in os.listdir(folder):
        f, e = os.path.splitext(infile)
        outfile = f"{f}.JPEG"
        if infile != outfile:
            try:
                with Image.open(infile) as im:
                    im.save(destination_dir + outfile)
            except OSError:
                print("cannot convert", infile)



def shape_rotate_img(folder):
    '''Change the parameters inside of the im.resize() and im.rotate() as necessary for sizing and rotating needs.'''
    for infile in os.listdir(folder):
        im = Image.open(infile)
        im = im.resize((600, 400))
        if im.mode != 'RGB':
            im.convert('RGB')