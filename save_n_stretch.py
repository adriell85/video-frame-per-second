import cv2
import math
import os
import numpy as np
from numba import njit

# CHANGE PATH INPUT AND RUN THE CODE ============================================================================================================================
# PATH INPUT ====================================================================================================================================================

videoPath = './light_day_occlusion/Channel2/Videos/'
STRETCH = True

# CODE ==========================================================================================================================================================
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


os.makedirs(videoPath[:-7]+'Frames')
framePath = videoPath[:-7]+'Frames'

for dirs, subdirs, files in os.walk(videoPath):
    for i, videoName in enumerate(files):
        os.makedirs(framePath+os.sep+videoName)
        video_framePath = framePath+os.sep+videoName

        cap= cv2.VideoCapture(videoPath+videoName)
        frameRate = cap.get(5) #frame rate

        cont = 0
        while(cap.isOpened()):
            frameId = cap.get(1) #current frame number
            ret, frame = cap.read()
            if ret == False:
                break
            if (frameId % math.floor(frameRate) == 0):
                cont += 1

                new_img = stretch(frame)

                cv2.imwrite(video_framePath+os.sep+'Frame'+str(cont)+'.png', frame)
                print('FRAME ' + str(cont) + ' SAVED')

                if STRETCH:
                    img = cv2.imread(video_framePath+os.sep+'Frame'+str(cont)+'.png', 1)

                    new_img = stretch(img)

                    print('FRAME ' + str(cont) + ' STRETCHED')
                    cv2.imwrite(video_framePath+os.sep+'Frame'+str(cont)+'.png', new_img)

        cap.release()
        print(videoName + ' Done!')