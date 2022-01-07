import os, sys
from PIL import Image, ImageFilter

jpg_folder = sys.argv[1]+"/"
png_folder = sys.argv[2]+"/"

if not os.path.exists(png_folder):
    os.makedirs(png_folder)
    
for jpg_file in os.listdir(jpg_folder):
    jpg_image = Image.open(f'{jpg_folder}{jpg_file}')
    png_file = os.path.splitext(jpg_file)[0]
    jpg_image.save(f'{png_folder}{png_file}.png', 'png')
    print(f'Converted {jpg_file}')