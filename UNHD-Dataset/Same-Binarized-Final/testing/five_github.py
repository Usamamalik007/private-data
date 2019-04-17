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

while aa<5:
    v=randint(1, 10)
    w=randint(1, 10)
    x=randint(1, 10)
    y=randint(1, 10)
    z=randint(1, 10)
    print(str(z)+","+str(w)+","+str(x)+","+str(y)+","+str(z)+",")
    img1 = cv2.imread("private-data/UNHD-Dataset/Same-Binarized-Final/testing/"+str(x)+'.png')
    img2 = cv2.imread("private-data/UNHD-Dataset/Same-Binarized-Final/testing/"+str(y)+'.png')
    img3 = cv2.imread("private-data/UNHD-Dataset/Same-Binarized-Final/testing/"+str(z)+'.png')
    img4 = cv2.imread("private-data/UNHD-Dataset/Same-Binarized-Final/testing/"+str(w)+'.png')
    img5 = cv2.imread("private-data/UNHD-Dataset/Same-Binarized-Final/testing/"+str(v)+'.png')
               
    vis = np.concatenate((img1, img2,img3,img4,img5), axis=1)
    cv2.imwrite("private-data/UNHD-Dataset/Same-Binarized-Final/testing/"+"_"+str(x)+"_"+str(y)+"_"+str(z)+"_"+str(w)+"_"+str(v)+'.png', vis)
    with open("private-data/UNHD-Dataset/Same-Binarized-Final/testing/"+"_"+str(x)+"_"+str(y)+"_"+str(z)+"_"+str(w)+"_"+str(v)+'.gt.txt', 'w',encoding="utf-8") as f:
        with open("private-data/UNHD-Dataset/Same-Binarized-Final/testing/"+str(x)+'.gt.txt', 'r',encoding="utf-8") as myfile:
            a=myfile.read()
        with open("private-data/UNHD-Dataset/Same-Binarized-Final/testing/"+str(y)+'.gt.txt', 'r',encoding="utf-8") as myfile:
            b=myfile.read()
        with open("private-data/UNHD-Dataset/Same-Binarized-Final/testing/"+str(z)+'.gt.txt', 'r',encoding="utf-8") as myfile:
            c=myfile.read()
        with open("private-data/UNHD-Dataset/Same-Binarized-Final/testing/"+str(w)+'.gt.txt', 'r',encoding="utf-8") as myfile:
            d=myfile.read()
        with open("private-data/UNHD-Dataset/Same-Binarized-Final/testing/"+str(w)+'.gt.txt', 'r',encoding="utf-8") as myfile:
            e=myfile.read()
        

        f.write(str(e) + " "+str(d) + " "+str(c)+" "+str(b)+" "+str(a) )

        aa=aa+1


