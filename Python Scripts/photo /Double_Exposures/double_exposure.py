#README: give this script two image files of any size and it blends them, creating a cool double exposure effect

import sys
from PIL import Image
import os

FOLDER_PATH = '/Users/scot/Desktop/Double_Exposures'

#if sys.argv[1] == 0 or sys.argv[2] == 0:
#    print('Please provide two images for blending')

image_1 = Image.open(sys.argv[1])
image_2 = Image.open(sys.argv[2])

def Double_Exposure(image_1, image_2, alpha=.5):
    image_2 = image_2.resize(image_1.size)
    return Image.blend(image_1, image_2, alpha)

file_name = '/double_exposure_' + str(len(os.listdir(FOLDER_PATH))-1) + '.jpg'
Double_Exposure(image_1, image_2).save(FOLDER_PATH + file_name)
