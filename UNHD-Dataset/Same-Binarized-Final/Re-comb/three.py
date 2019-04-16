from PIL import Image
import os
import cv2
import numpy as np
from random import randint

aa=0
w=0
x=0
y=0
z=0

while aa<2000:

    x=randint(1, 1464)
    y=randint(1, 1464)
    z=randint(1, 1464)
    print(str(x)+","+str(y)+","+str(z)+",")
    img1 = cv2.imread(str(x)+'.png')
    img2 = cv2.imread(str(y)+'.png')
    img3 = cv2.imread(str(z)+'.png')	
               
    vis = np.concatenate((img1, img2,img3), axis=1)
    cv2.imwrite("_"+str(x)+"_"+str(y)+"_"+str(z)+'.png', vis)
    with open("_"+str(x)+"_"+str(y)+"_"+str(z)+"_"+'.gt.txt', 'w',encoding="utf-8") as f:
        with open(str(x)+'.gt.txt', 'r',encoding="utf-8") as myfile:
            a=myfile.read()
        with open(str(y)+'.gt.txt', 'r',encoding="utf-8") as myfile:
            b=myfile.read()
        with open(str(z)+'.gt.txt', 'r',encoding="utf-8") as myfile:
            c=myfile.read()
        

        f.write(str(c)+" "+str(b)+" "+str(a) )

        aa=aa+1


