import os
from PIL import Image
import re
import argparse
from pathlib import Path


def resize_image(input_dir, infile, output_dir='resized', size=(150, 0)):

    if '.DS_Store' in infile:
        return

    output_file = os.path.splitext(infile)[0]
    exstension = os.path.splitext(infile)[1]

    try:
        img = Image.open(input_dir / infile)
        referance_size = size[0]
        widht = img.width
        heigth = img.height
        ratio = widht / heigth
        referanced_heigth = referance_size / ratio
        img = img.resize((referance_size, round(
            referanced_heigth)), Image.LANCZOS)

        new_file = output_dir + '/' + output_file + exstension
        rgb = img.convert('RGB')
        rgb.save(output_dir + '/' + output_file + '_t' + '.jpg')
        # img.save(new_file)
        print('image resized successfully')
    except IOError:
        print('unable to resize {}'.format(infile))


if __name__ == '__main__':

    output_dir = 'resized'
    dire = os.getcwd()
    # folder = 'Vintage'
    direc = f'/Users/kerimdeveci/Downloads/StaticImages'
    input_dir = 'images'
    full_input_dir = dire + '/' + input_dir

    # if not os.path.exists(os.path.join(dire, output_dir)):
    #     os.mkdir(output_dir)
    pathl = Path(direc)
    try:
        for file in os.listdir(direc):
            # print('file, {}'.format(file))
            resize_image(pathl, file, direc)
    except OSError:
        print('File Not Found')
