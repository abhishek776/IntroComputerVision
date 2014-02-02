from cv2_detect import detect
import cv2
import cv2.cv as cv
import os
 
 
def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
 
 
def run_detection(in_fn, out_fn):
    print ">>> Loading image..."
    img_color = cv2.imread(in_fn)
    img_gray = cv2.cvtColor(img_color, cv.CV_RGB2GRAY)
    img_gray = cv2.equalizeHist(img_gray)
    print in_fn, img_gray.shape
 
    print ">>> Detecting faces..."
    rects = detect(img_gray)
    print "Done"
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