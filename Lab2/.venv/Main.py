import cv2
import cv2 as cv
import numpy as np
## Задание 1-2
# cap=cv.VideoCapture(0)
# width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
# while True:
#     ok, img = cap.read()
#     if not(ok):
#         break
#     hsv=cv.cvtColor(img,cv.COLOR_RGB2HSV)
#     mask=cv.inRange(hsv,(0,155,155),(30,255,255))
#     outimg=cv2.bitwise_and(img,img,mask=mask)
#     cv.imshow('filtered',outimg)
#     if cv.waitKey(1) & 0XFF == 27:
#         break
# cv.destroyAllWindows()
# #Задание 3
# cap=cv.VideoCapture(0)
# kernel=np.zeros((5,5),np.uint8)
# kernel[5 // 2, :] = 1
# kernel[:, 5 // 2] = 1
# print(kernel)
# while True:
#     ok, img = cap.read()
#     if not(ok):
#         break
#     hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
#     out=cv.inRange(img,(0,155,155),(30,255,255))
#     Open=cv.morphologyEx(out,cv.MORPH_OPEN,kernel)
#     Close=cv.morphologyEx(out,cv.MORPH_CLOSE,kernel)
#     cv.imshow('Open',Open)
#     cv.imshow('Close',Close)
#     if cv.waitKey(1) & 0XFF == 27:
#         break
# cv.destroyAllWindows()
# #Задание 4-5
# cap=cv.VideoCapture(0)
# width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
# kernel=np.zeros((5,5),np.uint8)
# kernel[5 // 2, :] = 1
# kernel[:, 5 // 2] = 1
# while True:
#     ok, img = cap.read()
#     if not(ok):
#         break
#     hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
#     out=cv.inRange(hsv,(0,120,155),(30,255,255))
#     opened=cv.morphologyEx(out,cv.MORPH_OPEN,kernel)
#     moments=cv.moments(opened)
#     h,s,v=hsv[int(width/2),int(height//2)]
#     print(f"h:{h},s:{s},v:{v}")
#     if(moments["m00"]!=0):
#         print(f"S: {moments['m00']}")
#         print(f"Моменты 1 порядка: {moments['m01']}, {moments['m10']}")
#         xc=int(moments['m10']/moments['m00'])
#         yc=int(moments['m01']/moments['m00'])
#         (contours, _) = cv.findContours(opened.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#         for countour in contours:
#             (x, y, w, h) = cv.boundingRect(countour)
#             cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 4)
#             cv.rectangle(img,(xc-2,yc-2),(xc+2,yc+2),(255,255,255),2)
#     cv.imshow('Detecting red',img)
#     if cv.waitKey(1) & 0XFF == 27:
#         break
# cv.destroyAllWindows()