import cv2
import numpy as np
import time

count = 0
bg = "white"

rainbow = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 3\rainbow.jpg")

hsvcode = cv2.cvtColor(rainbow,cv2.COLOR_BGR2HSV)
lb1 = np.array([0,100,100])
ub1 = np.array([10,255,255])
lb2 = np.array([160,100,100])
ub2 = np.array([179,255,255])
lb3 = np.array([11,100,100])
ub3 = np.array([25,255,255])
lb4 = np.array([146,100,100])
ub4 = np.array([159,255,255])
lb5 = np.array([131,100,100])
ub5 = np.array([145,255,255])

mask1 = cv2.inRange(hsvcode,lb1,ub1)
mask2 = cv2.inRange(hsvcode,lb2,ub2)
mask3 = cv2.inRange(hsvcode,lb3,ub3)
mask4 = cv2.inRange(hsvcode,lb4,ub4)
mask5 = cv2.inRange(hsvcode,lb5,ub5)
maska = cv2.bitwise_or(mask1,mask2)
cv2.imshow("screen",maska)
maskb = cv2.bitwise_or(maska,mask3)
cv2.imshow("screen1",maskb)
maskc = cv2.bitwise_or(maskb,mask4)
cv2.imshow("screen2",maskc)
maskd = cv2.bitwise_or(maskc,mask5)
cv2.imshow("screen3",maskd)
kernel = np.ones((2,2),np.uint8)
mask = cv2.morphologyEx(maskd,cv2.MORPH_OPEN,kernel)
rainbow[mask>0]=[81,62,39]
cv2.imshow("screen4",rainbow)
cv2.waitKey(0)
cv2.destroyAllWindows()