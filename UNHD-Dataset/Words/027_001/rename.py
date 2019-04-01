
from PIL import Image
import os

with open('027_001_1_text.txt',encoding="utf-8") as f:
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

for filename in os.listdir("."):
    if(filename.endswith('.jpg')):
        abc=str(filename)
        print(filename + str(len(abc)))
        with open(filename[:-4]+'.gt.txt','w',encoding="utf-8") as myfile:
            myfile.write(content[c])
            c=c+1
