import cv2
import os
import numpy

print("OpenCV:", cv2.__version__)
print("cv2 location:", cv2.__file__)
print("Has face:", hasattr(cv2, "face"))

modfile = 'haarcascade_frontalface_default.xml'

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
        greyimg = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        if exists:
            face = facedetector.detectMultiScale(greyimg,scaleFactor=1.3,minNeighbors=4)
            for x,y,w,h in face:
                cv2.rectangle(image,(x-100,y-100),(x+w+75,y+h+100),(0,0,255),3)
                face = greyimg[y-100:y+h+100,x-100:x+w+75]
                cropped = cv2.resize(face,(width,height))
                filename = os.path.join(pics,"final"+str(count+1)+".png")
                cv2.imwrite(filename,cropped)
                count += 1
                cv2.imshow("screen",image)
                key = cv2.waitKey(0)
        else:
            print("doesn't exist")
    webcam.release()
'''images = []
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

height1 = 100
width1 = 100

(images,labels) = [numpy.array(i) for i in [images,labels]]

model = cv2.face.LBPHFaceRecognizer_create()
model.train(images,labels)

modfile = cv2.data.haarcascades+'haarcascade_frontalface_default.xml'
facedetector1 = cv2.CascadeClassifier(modfile)
webcam1 = cv2.VideoCapture(0)
count1 = 0
while True:
    exists1, image = webcam1.read()
    if exists1:
        face1 = facedetector1.detectMultiScale(image,scaleFactor=1.3,minNeighbors=4)
        for x1,y1,w1,h1 in face1:
            cv2.rectangle(face1,(x1-100,y1-100),(x1+w1+75,y1+h1+100),(0,0,255),3)
            face1 = image[y1-100,y1+h1+100,x1-100,x1+w1+75]
            cropped1 = cv2.resize(face1,(width1,height1))
            prediction = model.predict(cropped1)
            cv2.rectangle(face1,(x1-100,y1-100),(x1+w1+75,y1+h1+100),(0,255,0),3)
            if prediction[1]<100:
                cv2.putText(image,"%s -%.0f"%(names[prediction[0]],prediction[1]),(x1-150,y1-150),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0))
            else:
                cv2.putText(image,"person not recognised",(x1-150,y-150),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0))
        cv2.imshow("screen",image)
        key = cv2.waitKey(10)
        if key == 27:
            break'''
cv2.destroyAllWindows()
