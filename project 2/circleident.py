#preprocessing needed before equation
#colour mode, greyscale, blur(noise reduction)
import cv2
import numpy as np


#(x-k)2 + (y-h)2 = r2
oreye = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\eye.jpg",cv2.IMREAD_COLOR)
#reading image in colour
eye = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\eye.jpg",cv2.IMREAD_COLOR)
eye = cv2.cvtColor(eye,cv2.COLOR_BGR2GRAY)
eye = cv2.blur(eye,(3,3))

detcirc = cv2.HoughCircles(eye,
                           cv2.HOUGH_GRADIENT,
                           1,
                           20,
                           param1=50,
                           param2=30,
                           minRadius=1,
                           maxRadius=40)
#uint - unsigned integer 16, round circle values + converts into integer value

if detcirc is not None:
    detcirc = np.uint16(np.around(detcirc))
    #print(detcirc)
    for i in detcirc[0,:]:
        x,y,r = i[0],i[1],i[2]
        cv2.circle(oreye,(x,y),r,(0,0,255),3)
        cv2.circle(oreye,(x,y),1,(255,0,0),3)
        
cv2.imshow("screen",oreye)
cv2.waitKey(0)
