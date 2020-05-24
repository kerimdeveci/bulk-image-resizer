import os
from PIL import Image
import re
import argparse


def resize_image(input_dir, infile, output_dir='resized', size=(320, 180)):
    output_file = os.path.splitext(infile)[0] + '_resized'
    exstension = os.path.splitext(infile)[1]

    try:
        img = Image.open(input_dir + '/' + infile)
        img = img.resize((size[0], size[1]), Image.LANCZOS)

        new_file = output_dir + '/' + output_file + exstension
        img.save(new_file)
        print('image resized successfully')
    except IOError:
        print('unable to resize {}'.format(infile))


if __name__ == '__main__':

    output_dir = 'resized'
    dir = os.getcwd()
    input_dir = 'images'
    full_input_dir = dir + '/' + input_dir

    if not os.path.exists(os.path.join(dir, output_dir)):
        os.mkdir(output_dir)

    try:
        for file in os.listdir(full_input_dir):
            # print('file, {}'.format(file))
            resize_image(input_dir, file, output_dir)
    except OSError:
        print('File Not Found')
