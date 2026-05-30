#preprocessing needed before equation
#colour mode, greyscale, blur(noise reduction)
import cv2
import numpy as np


#(x-k)2 + (y-h)2 = r2
#orapple = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\appletree.jpg",cv2.IMREAD_COLOR)
#reading image in colour
apple = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\appletree.jpg",cv2.IMREAD_COLOR)
apple = cv2.cvtColor(apple,cv2.COLOR_BGR2GRAY)

block = cv2.SimpleBlobDetector_Params()
#applying an area filter
block.filterByArea = True
block.minArea = 100
#block.maxArea = 50

#applying circularity filter
block.filterByCircularity = True
block.minCircularity = 0.1

#apply convexity filter
block.filterByConvexity = True
block.minConvexity = 0.1

#inertia filter
block.filterByInertia = True
block.minInertiaRatio = 0.3

detector = cv2.SimpleBlobDetector_create(block)
keypoints = detector.detect(apple)
blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(apple,keypoints,blank,(255,0,0),cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)
blobsnum = len(keypoints)
print(blobsnum)
cv2.imshow("screen",blobs)
cv2.waitKey(0)

# circle - inertia ratio around 1
# ellipse - inertia ratio less than 1
# line - inertia ratio around 0








# apple = cv2.blur(apple,(3,3))

# detcirc = cv2.HoughCircles(apple,
#                            cv2.HOUGH_GRADIENT,
#                            1,
#                            20,
#                            param1=50,
#                            param2=30,
#                            minRadius=1,
#                            maxRadius=40)
# #uint - unsigned integer 16, round circle values + converts into integer value

# if detcirc is not None:
#     detcirc = np.uint16(np.around(detcirc))
#     #print(detcirc)
#     for i in detcirc[0,:]:
#         x,y,r = i[0],i[1],i[2]
#         cv2.circle(orapple,(x,y),r,(0,0,255),3)
#         cv2.circle(orapple,(x,y),1,(255,0,0),3)
#         cv2.imshow("screen",orapple)
#         cv2.waitKey(0)

