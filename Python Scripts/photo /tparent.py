from PIL import Image
import os
import sys

file = str(sys.argv[1])

img = Image.open(file)
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

file_name = os.path.splitext(file)

img.putdata(newData)
img.save((file_name[0] + '_tparent' + file_name[1]), "PNG")
