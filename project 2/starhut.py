import cv2
import numpy as np

country = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\country.jpg")

#drawing hut

country = cv2.rectangle(country,(350,300),(500,180),(10,10,230),-3)
country = cv2.line(country,(330,180),(425,110),(255,0,0),6)
country = cv2.line(country,(425,110),(520,180),(255,0,0),6)
country = cv2.line(country,(330,180),(520,180),(255,0,0),6)
array1 = np.array([[330,180],[425,110],[520,180]],np.int32)
cv2.fillPoly(country,[array1,array2],(255,0,0))
cv2.imshow("screen",country)
cv2.waitKey(0)

#drawing star

#country = cv2.line(country,(100,100),(130,100))