import time as t
import cv2 as cv 

image_flow = cv.VideoCapture(0)

while True:
    state,matlike = image_flow.read()

    y,x,c = matlike.shape

    center_x,center_y = x // 2, y // 2

    start_x,start_y = center_x - 100,center_y - 100
    stop_x,stop_y = center_x + 100,center_y + 100

    roi_image = matlike[start_x:stop_x,start_y:stop_y]


    cv.imshow('uA',roi_image)
    cv.waitKey(1)
