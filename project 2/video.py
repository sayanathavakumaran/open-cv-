import cv2
from PIL import Image
import os

path = r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\vidpics"
list1 = []
imglist = []
totalw = 0
totalh = 0

for x in os.listdir(path):
    print(x)
    if x.endswith(('.jpeg','.jpg','.png')):
        list1.append(x)
        #x = cv2.resize(x,(600,400))

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

for t in imglist:
    t = t.resize((meanw,meanh),Image.Resampling.LANCZOS)
    t.save(os.path.join(path,imglist))
print(imglist)