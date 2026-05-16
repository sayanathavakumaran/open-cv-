import cv2

#adding images

image1 = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\image1.jpg")
image2 = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\image2.jpg")
blend = cv2.addWeighted(image1,0.7,image2,0.3,0)
cv2.imshow("screen",blend)
cv2.waitKey(0)

#subtracting images

imagee1 = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\image1.jpg")
imagee2 = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\image2.jpg")
subtract = cv2.subtract(imagee2,imagee1)
cv2.imshow("screen",subtract)
cv2.waitKey(0)

#resizing images

imageee1 = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\image1.jpg")
imageee2 = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\image2.jpg")
cv2.imshow("screen",imageee1)
cv2.waitKey(0)
image1res = cv2.resize(imageee1,(1000,500))
cv2.imshow("screen",image1res)
cv2.waitKey(0)
cv2.imshow("screen",imageee2)
cv2.waitKey(0)
image2res = cv2.resize(imageee2,(250,125))
cv2.imshow("screen",image2res)
cv2.waitKey(0)
