import cv2

sunset = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\beach.webp")


sunset = cv2.line(sunset,(0,0),(1920,1080),(140,7,25),9)
#rectangl only requires 2 points
sunset = cv2.rectangle(sunset,(0,0),(960,540),(148,2,245),3)
sunset = cv2.rectangle(sunset,(1920,1080),(900,500),(208,245,2),-3)

cv2.imshow("screen",sunset)
cv2.waitKey(0)