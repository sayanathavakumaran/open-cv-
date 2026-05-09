import cv2

#reading + showing image
image = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\image1.jpg")
cv2.imshow("screen",image)
cv2.waitKey(0)

#resizing image
image1 = cv2.resize(image,(1000,500))
cv2.imshow("screen",image1)
cv2.waitKey(0)

#splitting the image into 3 colours
#showing blue saturated image
blue, green, red = cv2.split(image)
cv2.imshow("blue saturated image", blue)
cv2.waitKey(0)

#showing green saturated image
cv2.imshow("green saturated image", green)
cv2.waitKey(0)

#showing red saturated image
cv2.imshow("red saturated image", red)
cv2.waitKey(0)

#rotating the image
squareimg = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\squaredim.jpg")
square2 = cv2.resize(squareimg,(512,512))
rows, columns = square2.shape[:2]
image2 = cv2.getRotationMatrix2D((columns/2,rows/2),-45,1)
rotated = cv2.warpAffine(square2,image2,(columns,rows))
cv2.imshow("screen",rotated)
cv2.waitKey(0)


#drawing outline of image
outline = cv2.Canny(square2,5,100)
cv2.imshow("outlined",outline)
cv2.waitKey(0)