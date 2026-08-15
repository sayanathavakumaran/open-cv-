import cv2
import os

modfile = cv2.data.haarcascades+'haarcascade_frontalface_default.xml'
count = 0
folder = os.path.dirname(os.path.abspath(__file__))
name = input("whose pictures are you going to take? ")
pics = os.path.join(folder,name)
if os.path.isdir(name):
    print("already exists")
else:
    os.makedirs(pics,exist_ok=True)
    height = 100
    width = 100
    facedetector = cv2.CascadeClassifier(modfile)
    webcam = cv2.VideoCapture(0)
    while count < 5:
        exists, image= webcam.read()
        if exists:
            face = facedetector.detectMultiScale(image,scaleFactor=1.3,minNeighbors=4)
            for x,y,w,h in face:
                cv2.rectangle(image,(x-100,y-100),(x+w+75,y+h+100),(0,0,255),3)
                face = image[y-100:y+h+100,x-100:x+w+75]
                cropped = cv2.resize(face,(width,height))
                filename = os.path.join(pics,"final"+str(count+1)+".png")
                cv2.imwrite(filename,cropped)
                count += 1
            cv2.imshow("screen",image)
            key = cv2.waitKey(0)
    webcam.release()
images = []
labels = []
names = {}
id = 0
for subdir,dir,file in os.walk(folder):
    for sub in dir:
        names[id] = sub
        path = os.path.join(folder,sub)
        for filename in os.listdir(path):
            newpath = path+"/"+filename
            label = id
            images.append(cv2.imread(newpath,0))
            labels.append(label)
        id += 1
cv2.destroyAllWindows()

#pizza different toppings
#radio button checkbox
#choose size of pizza
#design own pizza ordering system with size topping
#    display order + price, tkinter