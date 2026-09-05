import cv2

video = cv2.VideoCapture('vid.mp4')
cascade = cv2.CascadeClassifier('cars.xml')

while True:
    exists, image = video.read()
    grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cars = cascade.detectMultiScale(grey,1.1,1)
    for x,y,w,h in cars:
        carrect = cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow('screen',image)
    if cv2.waitKey(10) == 27:
        break
cv2.destroyAllWindows()