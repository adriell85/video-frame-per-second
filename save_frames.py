import cv2
import math
 
# Path and name of video
videoPath = './Channel2/light_day_clear/Videos/'
videoName = 'MHDX_ch2_Main_20200206162704_20200206163100.mp4'

# Path of output frames
framePath = './Channel2/light_day_clear/Frames/'

# Capture video
cap= cv2.VideoCapture(videoPath+videoName)
frameRate = cap.get(5) # Frame rate


cont = 0
while(cap.isOpened()):
    frameId = cap.get(1) # Current frame number
    ret, frame = cap.read()
    if ret == False:
        break
    if (frameId % math.floor(frameRate) == 0): # Save 1 frame per video second
        cont += 1
        cv2.imwrite(framePath+videoName[:-4]+'_Frame'+str(cont)+'.png', frame)
        print(str(cont) + ' FRAMES SAVED')

cap.release()
print("Done!")
