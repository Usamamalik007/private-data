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
    w=randint(1, 1464)
    x=randint(1, 1464)
    y=randint(1, 1464)
    z=randint(1, 1464)
    print(str(w)+","+str(x)+","+str(y)+","+str(z)+",")
    img1 = cv2.imread("private-data/UNHD-Dataset/Same-Binarized-Final/Re-comb/"+str(x)+'.jpg')
    img2 = cv2.imread("private-data/UNHD-Dataset/Same-Binarized-Final/Re-comb/"+str(y)+'.jpg')
    img3 = cv2.imread("private-data/UNHD-Dataset/Same-Binarized-Final/Re-comb/"+str(z)+'.jpg')
    img4 = cv2.imread("private-data/UNHD-Dataset/Same-Binarized-Final/Re-comb/"+str(w)+'.jpg')	
               
    vis = np.concatenate((img1, img2,img3,img4), axis=1)
    cv2.imwrite("private-data/UNHD-Dataset/Same-Binarized-Final/Re-comb/"+"_"+str(x)+"_"+str(y)+"_"+str(z)+"_"+str(w)+'.jpg', vis)
    with open("private-data/UNHD-Dataset/Same-Binarized-Final/Re-comb/"+"_"+str(x)+"_"+str(y)+"_"+str(z)+"_"+str(w)+'.gt.txt', 'w',encoding="utf-8") as f:
        with open("private-data/UNHD-Dataset/Same-Binarized-Final/Re-comb/"+str(x)+'.gt.txt', 'r',encoding="utf-8") as myfile:
            a=myfile.read()
        with open("private-data/UNHD-Dataset/Same-Binarized-Final/Re-comb/"+str(y)+'.gt.txt', 'r',encoding="utf-8") as myfile:
            b=myfile.read()
        with open("private-data/UNHD-Dataset/Same-Binarized-Final/Re-comb/"+str(z)+'.gt.txt', 'r',encoding="utf-8") as myfile:
            c=myfile.read()
        with open("private-data/UNHD-Dataset/Same-Binarized-Final/Re-comb/"+str(w)+'.gt.txt', 'r',encoding="utf-8") as myfile:
            d=myfile.read()

        f.write(str(d) + " "+str(c)+" "+str(b)+" "+str(a) )

        aa=aa+1


