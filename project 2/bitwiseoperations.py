import cv2

#bitwise and operator
bit1 = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\1bit.png")
bit2 = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\2bit.png")
andblend = cv2.bitwise_and(bit1,bit2)
cv2.imshow("screen",andblend)
cv2.waitKey(0)

#bitwise or operator
bitt1 = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\1bit.png")
bitt2 = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\2bit.png")
orblend = cv2.bitwise_or(bitt1,bitt2)
cv2.imshow("screen",orblend)
cv2.waitKey(0)

#bitwise xor
bittt1 = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\1bit.png")
bittt2 = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\2bit.png")
xorblend = cv2.bitwise_xor(bittt1,bittt2)
cv2.imshow("screen",xorblend)
cv2.waitKey(0)

#bitwise xor
bitttt1 = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\1bit.png")
bitttt2 = cv2.imread(r"C:\Users\koval\Desktop\jetlearn python\open cv\project 2\2bit.png")
notbit1 = cv2.bitwise_not(bitttt1)
cv2.imshow("screen",notbit1)
cv2.waitKey(0)
notbit2 = cv2.bitwise_not(bitttt2)
cv2.imshow("screen",notbit2)
cv2.waitKey(0)