import cv2

country = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\country.jpg")
goat = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\goat.jpg")
country = cv2.resize(country,(goat.shape[1],goat.shape[0]))

'''
#subtract pixel values from one another
subtract = cv2.subtract(goat,country)
cv2.imshow("screen",subtract)

#adding pixel values from both images
addition = cv2.add(country,goat)
cv2.imshow("screen",addition)
cv2.waitKey(0)

#mixing images smoothly
blend = cv2.addWeighted(country,0.9,goat,0.1,0)
cv2.imshow("screen",blend)
cv2.waitKey(0)

#converting image to greyscale
greyscale = cv2.cvtColor(goat,cv2.COLOR_BGR2GRAY)
cv2.imshow("screen",greyscale)
cv2.waitKey(0)

#outline
outline = cv2.Canny(goat,100,5)
cv2.imshow("outlined",outline)
cv2.waitKey(0)
'''

#blurring
gaussianblur = cv2.GaussianBlur(goat,(101,101),0)
cv2.imshow("blurred",gaussianblur)
cv2.waitKey(0)

medianblur = cv2.medianBlur(goat,(101))
cv2.imshow("blurred",medianblur)
cv2.waitKey(0)
