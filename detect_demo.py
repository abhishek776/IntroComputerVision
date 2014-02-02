"""
This is a program that parses through every foot in
the Pictures directory, recognizes where the faces are, draws
rectangles around the faces, and writes each new image to the
OutputPictures directory. There are some sample photos that I have ran
in the directories provided.
"""

from cv2_detect import detect
import cv2
import cv2.cv as cv
import os
 
 
def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
 
 
def run_detection(in_fn, out_fn):
    img_color = cv2.imread(in_fn)
    img_gray = cv2.cvtColor(img_color, cv.CV_RGB2GRAY)
    img_gray = cv2.equalizeHist(img_gray) 
    rects = detect(img_gray)
    print "Copied " + in_fn + " to " + out_fn 
    img_out = img_color.copy()
    draw_rects(img_out, rects, (0, 255, 0))
    cv2.imwrite(out_fn, img_out)
 
 
def main():
    file_paths = []
    files = [f for f in os.listdir('./Pictures')]
    for f in files:
        if f.endswith((".jpg")):
            file_paths.append(f)

    for fil in file_paths:
        run_detection('Pictures/' + fil, 'OutputPictures/modified_' + fil)

 
if __name__ == '__main__':
    main()