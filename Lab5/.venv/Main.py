import cv2 as cv
def blur_bw(img):
    bw=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    blured=cv.GaussianBlur(bw,(5,5),10)
    return blured
cap=cv.VideoCapture("ЛР4_main_video.mov")
ok, img=cap.read()

fps = cap.get(cv.CAP_PROP_FPS)
width=int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

fourcc = cv.VideoWriter_fourcc(*'mp4v')
video_writer = cv.VideoWriter("output.mp4", fourcc, fps, (width, height))

old=blur_bw(img)
while True:
    ok,frame=cap.read()
    if not ok:
        break
    new=blur_bw(frame)

    frame_diff=cv.absdiff(old,new)
    thres=cv.threshold(frame_diff,50,255,cv.THRESH_BINARY)[1]
    contours,_=cv.findContours(thres,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    try:
        cnt=contours[0]
        area=cv.contourArea(cnt)
        if area>40:
            cv.imshow('frame',frame_diff)
            cv.imshow('thres',thres)
            cv.waitKey(0)
            print("contour found")
            video_writer.write(frame)
    except:
        print()
    old=new
cap.release()
cv.destroyAllWindows()