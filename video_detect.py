from cv2_detect import detect
import cv2
import cv2.cv as cv
import numpy as np
import os
 
 
def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
 
 
def run_detection():
    cap = cv2.VideoCapture(0)
    rects = None
    counter = 10
    while(True):
        ret, frame = cap.read()
        img_gray = cv2.cvtColor(frame,cv.CV_RGB2GRAY)
        img_gray = cv2.equalizeHist(img_gray)

        if(counter == 10):
            rects = detect(img_gray)
            counter = 0
        counter = counter + 1
        draw_rects(frame, rects, (0,255,0))
        cv2.imshow('feed',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def main():
    run_detection()

if __name__ == '__main__':
    main()