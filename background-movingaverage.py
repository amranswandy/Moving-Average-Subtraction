import cv2
import video
import sys
import numpy as np


if __name__ == '__main__':
    print ('__doc__')

    try: fn = sys.argv[1]
    except: fn = 0

    def nothing(*arg):
        pass

    cv2.namedWindow('bgmodel')
    cv2.namedWindow('foregound')
    cv2.namedWindow('input')
    cv2.createTrackbar('Size of buffer', 'bgmodel', 110, 500, nothing)
    cv2.createTrackbar('Difference threshold', 'bgmodel', 10, 200, nothing)
    n=0

    cap = video.create_capture('Layur.mp4')

    flag, img = cap.read()
    movingaverage=np.float32(img)
    while True:
        flag, img = cap.read()

        fbuffer=cv2.getTrackbarPos('Size of buffer', 'bgmodel')
        if fbuffer==0:
            fbuffer=1
        alpha=float(1.0/fbuffer) 
        cv2.accumulateWeighted(img,movingaverage,alpha)
        res=cv2.convertScaleAbs(movingaverage)
        cv2.imshow('bgmodel', res)

        tmp= cv2.resize(img, (0,0), fx=0.5, fy=0.5)
        cv2.imshow('input', tmp)

        difference_img = cv2.absdiff(res, img)

        grey_difference_img = cv2.cvtColor(difference_img, cv2.COLOR_BGR2GRAY)
        difference_thresh=cv2.getTrackbarPos('Difference threshold', 'bgmodel')
        ret,th1 = cv2.threshold(grey_difference_img,difference_thresh,255,cv2.THRESH_BINARY)
        cv2.imshow('foregound',th1)
        n+=1

        ch = cv2.waitKey(5)
        if ch == 27:
            break
    cv2.destroyAllWindows()
