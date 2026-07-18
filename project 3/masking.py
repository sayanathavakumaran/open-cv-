import cv2
import numpy as np
import time

count = 0
bg = "white"

rose = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 3\rosepot.jpg")

hsvcode = cv2.cvtColor(rose,cv2.COLOR_BGR2HSV)
lb1 = np.array([0,100,100])
ub1 = np.array([10,255,255])
lb2 = np.array([160,100,100])
ub2 = np.array([179,255,255])

mask1 = cv2.inRange(hsvcode,lb1,ub1)
mask2 = cv2.inRange(hsvcode,lb2,ub2)
mask = cv2.bitwise_or(mask1,mask2)
kernel = np.ones((5,5),np.uint8)
mask = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
rose[mask>0]=[255,255,255]
cv2.imshow("screen",rose)
cv2.waitKey(0)
cv2.destroyAllWindows()