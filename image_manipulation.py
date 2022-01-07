import os
from PIL import Image, ImageFilter

img = Image.open('pokemon/pikachu.jpg')

img_blurred = img.filter(ImageFilter.BLUR)

img_blurred.save('pokemon/pikachu_blurred.jpg')
