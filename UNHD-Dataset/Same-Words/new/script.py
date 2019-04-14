from PIL import Image
from resizeimage import resizeimage
import os

count=0
for filename in os.listdir("."):
    if filename.endswith("g"):
        # print(os.path.join(directory, filename))
        fd_img = open(filename, 'r+b')
        img = Image.open(fd_img)
        width, height = img.size
        img.close()
        if height<100:
            count=count+1
            print filename
            os.remove(filename)


print count
