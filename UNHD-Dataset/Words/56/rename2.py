
from PIL import Image
import os
import glob, os

import re
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

with open('56.txt',encoding="utf-8") as f:
    content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]


print(type(content))

c=0


for filename in os.listdir("."):
    if(filename.endswith('.jpg')):
        if(len(filename)==22):
            print(filename[:-6]+'9'+filename[-5:])
            os.rename(filename,filename[:-6]+'9'+filename[-5:])
            continue

aa=1

for filename in os.listdir("."):
    if(filename.endswith('.jpg')):
        print("here "+filename)
        os.rename(filename,"56_"+str(aa)+".jpg")
        aa=aa+1


for filename in sorted(glob.glob('*.jpg'), key=numericalSort):
    print("here2 "+filename)
    abc=str(filename)
    print(filename + str(len(abc)))
    with open(filename[:-4]+'.gt.txt','w',encoding="utf-8") as myfile:
        myfile.write(content[c])
        c=c+1


