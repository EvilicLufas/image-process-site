from __future__ import print_function
import numpy as np
import matplotlib
import cv2 as cv
import argparse
import math

# parser = argparse.ArgumentParser(description = 'Code for Feature Detection tutorial.')
# parser.add_arguement('--input', help ='Path to input image', defualt = 'person_dancing_test.png');
# args = parser.parse_args()

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='my-initial-scripts Resize Video')
    parser.add_argument('--video', type=str, default='')
    parser.add_argument('--resolution', type=str, default='432x368', help='resolution to resize video to, default is 432x368')
    parser.add_argument('--newfile', type=str, default='resizedvid.mp4')
    args = parser.parse_args()

    cap = cv.VideoCapture(args.video)
    resolutions = args.resolution.split('x')
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    writer = cv.VideoWriter(args.newfile, fourcc, 30, (int(resolutions[0]),int(resolutions[1])))
    w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    if ~cap.isOpened():
        print("Error opening the video stream or file")
    while cap.isOpened():
        ret_val, image = cap.read()
        if ret_val == True:
            newWidth = round(h*int(resolutions[0])/int(resolutions[1]))
            image = image[0:h, (0+((w-newWidth)//2)):(w-((w-newWidth)//2))]
            newImg = cv.resize(image, (int(resolutions[0]),int(resolutions[1])),fx=0,fy=0,interpolation=cv.INTER_AREA)
            writer.write(newImg)
        else:
            print("ret_val not true")
            break
    cap.release()
    writer.release()
    cv.destroyAllWindows()