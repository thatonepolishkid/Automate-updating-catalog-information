#!/usr/bin/env python3
import os
from PIL import Image

folder_dir = r'C:/Users/Marcin Malek/Desktop/phone_pictures/'
destination_dir = r'C:/Users/Marcin Malek/Desktop/move pictures to folder/'

def change_image(folder_dir):
    for file in os.listdir(folder_dir):
        if file.endswith(".tiff"):
            split_file = file.split(".")
            name = f"{split_file[0]}.jpeg"
            im = Image.open(folder_dir + file).convert("RGB")
            im.resize((600, 400)).save(f"{folder_dir}{name}", "JPEG")


os.chdir(folder_dir)
change_image(folder_dir)
