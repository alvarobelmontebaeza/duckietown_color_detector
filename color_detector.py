#!/usr/bin/env python3
import cv2
import numpy as np
from time import sleep
import os
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(2)
n_splits = int(os.environ['N_SPLITS'])

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Change color space to HSV, as it allows easier color distinction by
    # looking at the Hue channel, which indicates the color.
    hsv_image = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # h, s, v = cv2.split(hsv_image)
    split_size = len(hsv_image)/n_splits

    # Obtain color distribution in each horizontal split.
    for i in range(n_splits):
        first_row = int(i*split_size)
        last_row = int((i+1) * split_size)
        colorHist = []
        
        segment = hsv_image[first_row:last_row, :,:]

        # ----------- APPLY COLOR FILTERING ----------
        # Check for the current image segment what is 
        # the most present color among the most common
        # colors in duckietown: Black (road), Yellow, 
        # White (lines/leds), Red (duckiebots), Blue

        ####### Apply Black filtering ########

        # define range of black color in HSV
        lower_black = np.array([0,0,0])
        upper_black = np.array([0,0,75])

        # Threshold the HSV image to get only black colors
        mask_black = cv2.inRange(hsv_image, lower_black, upper_black)

        # Bitwise-AND mask and original image
        black = cv2.bitwise_and(hsv_image,hsv_image, mask= mask_black)

        ####### Apply Blue filtering #########

        # define range of blue color in HSV
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])

        # Threshold the HSV image to get only blue colors
        mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)

        # Bitwise-AND mask and original image
        blue = cv2.bitwise_and(hsv_image,hsv_image, mask= mask_blue)
        
        ########## Apply Yellow filtering ##########

        # define range of yellow color in HSV
        lower_yellow = np.array([20,50,50])
        upper_yellow = np.array([40,255,255])

        # Threshold the HSV image to get only yellow colors
        mask_yellow = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

        # Bitwise-AND mask and original image
        yellow = cv2.bitwise_and(hsv_image,hsv_image, mask= mask_yellow)

        # Apply White filtering

        # define range of white color in HSV
        lower_white = np.array([0,0,125])
        upper_white = np.array([0,0,255])

        # Threshold the HSV image to get only white colors
        mask_white = cv2.inRange(hsv_image, lower_white, upper_white)

        # Bitwise-AND mask and original image
        white = cv2.bitwise_and(hsv_image,hsv_image, mask= mask_white)

        # Apply Red filtering.

        # define range of red color in HSV
        lower_red = np.array([0,50,50])
        upper_red = np.array([10,255,255])

        mask1 = cv2.inRange(hsv_image, lower_red, upper_red)

        lower_red = np.array([170,50,50])
        upper_red = np.array([179,255,255])

        mask2 = cv2.inRange(hsv_image, lower_red, upper_red)

        # mix both masks to obtain full red range mask
        mask_red = mask1 or mask2

        # Bitwise-AND mask and original image
        red = cv2.bitwise_and(hsv_image,hsv_image, mask= mask_red)

    # Set 1 Hz frequency
    sleep(1)


cap.release()
cv2.destroyAllWindows()
