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

while aa<1000:
 
    y=randint(1, 1464)
    z=randint(1, 1464)
    print(str(y)+","+str(z)+",")

    img2 = cv2.imread("private-data/UNHD-Dataset/Same-Binarized-Final/Recomb/"+str(y)+'.jpg')
    img3 = cv2.imread("arabic-6000/"+str(z)+'.jpg')
	
               
    vis = np.concatenate((img2,img3), axis=1)
    cv2.imwrite("private-data/UNHD-Dataset/Same-Binarized-Final/Recomb/"+"_"+str(y)+"_"+str(z)+'.jpg', vis)
    with open("private-data/UNHD-Dataset/Same-Binarized-Final/Recomb/"+"_"+str(y)+"_"+str(z)+'.gt.txt', 'w',encoding="utf-8") as f:
        with open("private-data/UNHD-Dataset/Same-Binarized-Final/Recomb/"+str(y)+'.gt.txt', 'r',encoding="utf-8") as myfile:
            b=myfile.read()
        with open("private-data/UNHD-Dataset/Same-Binarized-Final/Recomb/"+str(z)+'.gt.txt', 'r',encoding="utf-8") as myfile:
            c=myfile.read()
        f.write(str(c)+" "+str(b) )

        aa=aa+1


