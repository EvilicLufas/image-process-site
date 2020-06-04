from __future__ import print_function
import numpy as np
import matplotlib
import cv2 as cv

# parser = argparse.ArgumentParser(description = 'Code for Feature Detection tutorial.')
# parser.add_arguement('--input', help ='Path to input image', defualt = 'person_dancing_test.png');
# args = parser.parse_args()

cap = cv.VideoCapture('tiktok_comp.mp4')

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    diff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv.threshold(blur, 10, 255, cv.THRESH_BINARY)
    dilated = cv.dilate(thresh, None, iterations=3)
    contours, _ = cv.findContours(dilated, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(frame1, contours, -1, (0,0,255), 2)

    cv.imshow("feed", frame1)
    frame1 = frame2
    _, frame2 = cap.read()

    if cv.waitKey(40) == 27:
        break
cv.destroyAllWindows()
cap.release()