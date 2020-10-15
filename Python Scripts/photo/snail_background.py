import sys
from PIL import Image
import random

height_by_snail = 20

def make_square(im, min_size=256, fill_color=(255, 255, 255, 0)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im

file_path = "/Users/scot/Desktop/momentous/assets/Snail Photos/"
images = [make_square(Image.open(file_path + x)) for x in [str(i) + '.png' for i in range(1,32)]]

def gen_row(images):
    widths, heights = zip(*(im.size for im in images))
    
    total_width = sum(widths)
    max_height = max(heights)
    
    random.shuffle(images)
    
    new_im = Image.new('RGBA', (total_width, max_height), (255, 255, 255, 0))
    
    x_offset = 0
    for im in images:
        new_im.paste(im.rotate(random.randint(0,360)), (x_offset,0))
        x_offset += im.size[0]
    
    return new_im

def get_concat_v(im1, im2):
    dst = Image.new('RGBA', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst
    
#get_concat_v(gen_row(images), gen_row(images))

bg = Image.new('RGBA', (gen_row(images).width, 575*height_by_snail))
for i in range(height_by_snail):
    bg.paste(gen_row(images), (0, 575*i))

bg.save('snail_background_20.png')
