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

while aa<10000:
    u=randint(1, 2364)
    v=randint(1, 2364)
    w=randint(1, 2364)
    x=randint(1, 2364)
    y=randint(1, 2364)
    z=randint(1, 2364)
    print(str(z)+","+str(w)+","+str(x)+","+str(y)+","+str(z)+",")
    img1 = cv2.imread("private-data/UNHD-Dataset/Same-Binarized-Final/Re-comb/"+str(x)+'.png')
    img2 = cv2.imread("private-data/UNHD-Dataset/Same-Binarized-Final/Re-comb/"+str(y)+'.png')
    img3 = cv2.imread("private-data/UNHD-Dataset/Same-Binarized-Final/Re-comb/"+str(z)+'.png')
    img4 = cv2.imread("private-data/UNHD-Dataset/Same-Binarized-Final/Re-comb/"+str(w)+'.png')
    img5 = cv2.imread("private-data/UNHD-Dataset/Same-Binarized-Final/Re-comb/"+str(v)+'.png')
    img6 = cv2.imread("private-data/UNHD-Dataset/Same-Binarized-Final/Re-comb/"+str(u)+'.png')
	
    vis = np.concatenate((img1, img2,img3,img4,img5,img6), axis=1)
    cv2.imwrite("private-data/UNHD-Dataset/Same-Binarized-Final/Re-comb/"+"_"+str(x)+"_"+str(y)+"_"+str(z)+"_"+str(w)+"_"+str(v)+"_"+str(u)+'.png', vis)
    with open("private-data/UNHD-Dataset/Same-Binarized-Final/Re-comb/"+"_"+str(x)+"_"+str(y)+"_"+str(z)+"_"+str(w)+"_"+str(v)+"_"+str(u)+'.gt.txt', 'w',encoding="utf-8") as f:
        with open("private-data/UNHD-Dataset/Same-Binarized-Final/Re-comb/"+str(x)+'.gt.txt', 'r',encoding="utf-8") as myfile:
            a=myfile.read()
        with open("private-data/UNHD-Dataset/Same-Binarized-Final/Re-comb/"+str(y)+'.gt.txt', 'r',encoding="utf-8") as myfile:
            b=myfile.read()
        with open("private-data/UNHD-Dataset/Same-Binarized-Final/Re-comb/"+str(z)+'.gt.txt', 'r',encoding="utf-8") as myfile:
            c=myfile.read()
        with open("private-data/UNHD-Dataset/Same-Binarized-Final/Re-comb/"+str(w)+'.gt.txt', 'r',encoding="utf-8") as myfile:
            d=myfile.read()
        with open("private-data/UNHD-Dataset/Same-Binarized-Final/Re-comb/"+str(w)+'.gt.txt', 'r',encoding="utf-8") as myfile:
            e=myfile.read()
        with open("private-data/UNHD-Dataset/Same-Binarized-Final/Re-comb/"+str(w)+'.gt.txt', 'r',encoding="utf-8") as myfile:
            ff=myfile.read()
        

        f.write(str(ff) + " "+str(e) + " "+str(d) + " "+str(c)+" "+str(b)+" "+str(a) )

        aa=aa+1


