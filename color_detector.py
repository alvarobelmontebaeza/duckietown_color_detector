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
    colorHist = np.array([[],[],[]])

    # Obtain color distribution in each horizontal split.
    for i in range(n_splits):
        first_row = int(i*split_size)
        last_row = int((i+1) * split_size))
        
        segment = hsv_image[first_row:last_row, :]

        # Obtain color histogram. 
        # params: (image,channels,...,bins,range)
        colorHist[i,:,:] = cv2.calcHist([hsv_image],[0,1],None,[180,256],[0,180,0,256])
    
    cv2.imshow(frame)
    plt.imshow(colorHist,interpolation = 'nearest')
    plt.show()

    # Set 1 Hz frequency
    sleep(1)

cap.release()
cv2.destroyAllWindows()
