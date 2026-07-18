import cv2
from PIL import Image
import os
import random

path = r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\vidpics"
list1 = []
imglist = []
totalw = 0
totalh = 0

type = input("do you want your video repeated or shuffled: ")

for x in os.listdir(path):
    print(x)
    if x.endswith(('.jpeg','.jpg','.png')):
        list1.append(x)
        #x = cv2.resize(x,(600,400))

print(len(list1))
print(list1)
meanw = 0
meanh = 0

for i in range(len(list1)):
    img = Image.open(os.path.join(path,list1[i]))
    imglist.append(img)
    sizew, sizeh = img.size
    totalw += sizew
    totalh += sizeh

    
meanw = totalw//len(list1)
print(meanw)
meanh = totalh//len(list1)
print(meanh)

for t in range(len(imglist)):
    b = imglist[t].resize((meanw,meanh),Image.Resampling.LANCZOS)
    b.save(os.path.join(path,list1[t]))
print(imglist)

if type == "shuffled":
    random.shuffle(list1)
    frame = cv2.imread(os.path.join(path,list1[0]))
    height,width,layers = frame.shape
    videob = cv2.VideoWriter(os.path.join(path,"video.avi"),cv2.VideoWriter_fourcc(*'XVID'),1,(width,height))
    videob.write(frame)
    for x in range(1,len(list1)):
        frame = cv2.imread(os.path.join(path,list1[x]))
        videob.write(frame)
elif type == "repeated":
    frame = cv2.imread(os.path.join(path,list1[0]))
    height,width,layers = frame.shape
    videob = cv2.VideoWriter(os.path.join(path,"video.avi"),cv2.VideoWriter_fourcc(*'XVID'),1,(width,height))
    videob.write(frame)
    for y in range(2):
        for x in range(1,len(list1)):
            frame = cv2.imread(os.path.join(path,list1[x]))
            videob.write(frame)

cv2.destroyAllWindows()
videob.release()