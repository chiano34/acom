import cv2
import cv2 as cv
#задание 1-2
# img=cv.imread("test.jpeg",cv.IMREAD_GRAYSCALE)
# img2=cv.imread("test.jpg",cv.IMREAD_REDUCED_GRAYSCALE_2)
# img3=cv.imread("test.png",cv.IMREAD_COLOR)
# cv.namedWindow('jpeg',cv.WINDOW_NORMAL)
# cv.namedWindow('jpg',cv.WINDOW_AUTOSIZE)
# cv.namedWindow('png',cv.WINDOW_FULLSCREEN)
# cv.imshow("jpeg",img)
# cv.imshow("jpg",img2)
# cv.imshow("png",img3)
# cv.waitKey(0)
# ## Задание 3-5
# cap=cv.VideoCapture("video.mp4")
# ok, img=cap.read()
# w=int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# h=int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
# fps = cap.get(cv.CAP_PROP_FPS)
#
# fourcc = cv.VideoWriter_fourcc(*'mp4v')  # Кодек для mp4
# video_writer = cv.VideoWriter("output.mp4", fourcc, fps, (w, h))
#
# while True:
#     ok,img=cap.read()
#     if not ok:
#         break
#     gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
#     gray=cv.resize(gray,(800,600))
#     cv.imshow('mp4',gray)
#     video_writer.write(img)
#     if cv.waitKey(1) & 0xFF == 27:
#         break
# cap.release()
# video_writer.release()
# frame=cv.imread("standart.png ")
# img_HSV=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
# cv.imshow("Standart",frame)
# cv.imshow("HSV",img_HSV)
# cv.waitKey(0)
# cv.destroyAllWindows()
# #Задание 6
# cap=cv.VideoCapture(0)
# ok, img=cap.read()
# fps = cap.get(cv.CAP_PROP_FPS)
# width=int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# height=int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
# # Создаем объект VideoWriter для записи видео
# fourcc = cv.VideoWriter_fourcc(*'mp4v')  # Кодек для mp4
# video_writer = cv.VideoWriter("output.mp4", fourcc, fps, (width, height))
# #Переменные для хранения координат прямоугольников для нахождения
# rect_width, rect_height = 70, 20  # Ширина и высота прямоугольников
# rect1p1=(int(width/2)-rect_height,int(height/2)-rect_width)
# rect1p2=(int(width/2)+rect_height,int(height/2)+rect_width)
# rect2p1=(int(width/2)-rect_width,int(height/2)-rect_height)
# rect2p2=(int(width/2)+rect_width,int(height/2)+rect_height)
#
# while True:
#     ok,img=cap.read()
#     if not ok:
#         break
#     cv2.rectangle(img,rect1p1,rect1p2,(0,0,255),2)
#     cv2.rectangle(img,rect2p1,rect2p2,(0,0,255),2)
#     video_writer.write(img)
#     cv.imshow('mp4',img)
#     if cv.waitKey(1) & 0xFF == 27:
#         break
#Задание 7
# cap=cv.VideoCapture(0)
# ok,img=cap.read()
# width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
# fourcc = cv.VideoWriter_fourcc(*'mp4v')
# video_writer = cv.VideoWriter("camera.mp4", fourcc, 25, (width, height))
# while True:
#     ok, img = cap.read()
#     if not(ok):
#         break
#     cv.imshow('mp4',img)
#     video_writer.write(img)
#     if cv.waitKey(1) & 0XFF == ord('q'):
#         break
# cap.release()
# cv.destroyAllWindows()
# #Задание 8
# cap=cv.VideoCapture(0)
# ok, img=cap.read()
# fps = cap.get(cv.CAP_PROP_FPS)
# width=int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# height=int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
# # Создаем объект VideoWriter для записи видео
# fourcc = cv.VideoWriter_fourcc(*'mp4v')  # Кодек для mp4
# video_writer = cv.VideoWriter("output.mp4", fourcc, fps, (width, height))
# #Переменные для хранения координат прямоугольников для нахождения
# rect_width, rect_height = 70, 20  # Ширина и высота прямоугольников
# rect1p1=(int(width/2)-rect_height,int(height/2)-rect_width)
# rect1p2=(int(width/2)+rect_height,int(height/2)+rect_width)
# rect2p1=(int(width/2)-rect_width,int(height/2)-rect_height)
# rect2p2=(int(width/2)+rect_width,int(height/2)+rect_height)
# while True:
#     ok,img=cap.read()
#     if not ok:
#         break
#     r,g,b=img[int(width/2),int(height//2)]
#     if(r>=b and r>=g):
#         color=(255,0,0)
#     elif(g>=r and g>=b):
#         color=(0,255,0)
#     elif(b>=r and b>=g):
#         color=(0,0,255)
#     cv2.rectangle(img,rect1p1,rect1p2,color,2)
#     cv2.rectangle(img,rect2p1,rect2p2,color,2)
#     video_writer.write(img)
#     cv.imshow('mp4',img)
#     if cv.waitKey(1) & 0xFF == 27:
#         break
# ##Задание 9
#
# cap=cv.VideoCapture("rtsp://192.168.0.70:8080/h264_pcm.sdp")
# while True:
#     ret, frame = cap.read()
#     if not(ret):
#         break
#     cv.imshow('mp4',frame)
#     if cv.waitKey(1) & 0XFF == 27:
#         break