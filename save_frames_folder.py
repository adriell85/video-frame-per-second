import cv2
import math
import glob
 
# Path and name of video
videoFolder = '/media/adriell/TRABALHOS/videosDowloaded/*.mp4'
outputFolder = '/media/adriell/TRABALHOS/videosDowloaded/Frames/'
# videoName = 'MHDX_ch2_Main_20200206162704_20200206163100.mp4'

for folder in glob.glob(videoFolder):


# Capture video
    cap= cv2.VideoCapture(folder)
    frameRate = cap.get(5) # Frame rate


    cont = 0
    while(cap.isOpened()):
        frameId = cap.get(1) # Current frame number
        ret, frame = cap.read()
        if ret == False:
            break
        if (frameId % math.floor(frameRate) == 0): # Save 1 frame per video second
            cont += 1
            cv2.imwrite(outputFolder+'_Frame'+str(cont)+'.png', frame)
            print(str(cont) + ' FRAMES SAVED')

    cap.release()
    print("Done!")
