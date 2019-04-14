from PIL import Image
from resizeimage import resizeimage
import os

for filename in os.listdir("."):
    if filename.endswith("g"):
        # print(os.path.join(directory, filename))
        fd_img = open(filename, 'r+b')
        img = Image.open(fd_img)
        width, height = im.size
        if height<48:
            count=count+1
            print filename


print count
