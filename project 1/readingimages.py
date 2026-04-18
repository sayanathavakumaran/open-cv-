import cv2
import os
rose = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 1\rose.jpg")
cv2.imshow("screen",rose)
cv2.waitKey(0)

#reading image in greyscale

rose1 = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 1\rose.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("screen1",rose1)
cv2.waitKey(0)

#saving image
path = r"C:\Users\koval\Desktop\jetlearn python\open cv\project 1"
os.chdir(path)

#writing image to the directory
cv2.imwrite("greyrose.jpg",rose1)
print("image saved successfully")
