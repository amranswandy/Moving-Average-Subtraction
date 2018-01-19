import cv2
import video
import common
import sys
import numpy as np

cv2.namedWindow('Layur.mp4')

cam = video.create_capture('Layur.mp4')

while True:
   # read an image from the video camera
   ret, img = cam.read()
  
   # put that image in the window 
   cv2.imshow('Layur.mp4', img)

   if 0xFF & cv2.waitKey(5) == 27:
      break


