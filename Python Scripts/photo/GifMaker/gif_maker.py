#this could EASILY be a twitter bot
from PIL import Image
import os

PATH = '/Users/scot/Desktop/GitHub/GifMaker/'
SIZE = 500,500

def OrientImage(image):
    exif = image._getexif()
    if exif == None:
        return image
        
    if exif.get(42035) == 'Apple':
        orientation = exif.get(274)
        if orientation == 1:
            return image
        elif orientation == 3:
            return image.rotate(180, expand=True)
        elif orientation == 6:
            return image.rotate(270, expand=True)
        elif orientation == 8:
            return image.rotate(90, expand=True)
    else:
        return image

def CreateGif(im, path, intervals=15, num_white_frames=0):
        im.save(path, save_all=True, append_images=[Image.eval(im, lambda i: 255 if i <= (j*intervals) else 0) for j in range(int(255/intervals)+num_white_frames)])


for image in [file for file in os.listdir(PATH + 'images/') if file[0] != '.']:
    im = Image.open(PATH + 'images/' + image)
    im = OrientImage(im)
    im.thumbnail(SIZE)
    file_name = PATH + 'gifs/' + os.path.splitext(image)[0] + '.gif'
    CreateGif(im, file_name, intervals=30, num_white_frames=1)
