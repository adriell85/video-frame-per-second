import cv2
import os
import numpy as np
from numba import njit

# Path of frames
framePath = './Channel2/light_day_clear/Frames/'

# Stretch function: turn image wide, duplicating number of columns
@njit
def stretch(img):
    rows, cols, channels = img.shape[:3]
    new_img = np.zeros((rows, cols*2, channels))
    for channel in range(channels):
        for row in range(rows):
            for col in range(0, cols*2, 2):
                new_img[row,col,channel] = img[row,int(col/2),channel]
                new_img[row,col+1,channel] = img[row,int(col/2),channel]
    return new_img


# Stretch all images in folder
for dirs, subdirs, files in os.walk(framePath):
    for i, frame_name in enumerate(files):
        img = cv2.imread(framePath+frame_name, 1)

        new_img = stretch(img)

        print(frame_name + ' NEW IMAGE SAVED')
        cv2.imwrite(framePath+frame_name, new_img)