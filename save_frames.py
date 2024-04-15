import cv2
import numpy as np
import dv_processing as dv
import time
from datetime import datetime

# Open the webcam
cap = cv2.VideoCapture(0)
capture = dv.io.CameraCapture(cameraName="DAVIS346_00000448")


change_thresh = 10

# Initialize frame count
frame_count = 0

prev_frame = capture.getNextFrame()

while prev_frame is None:
    prev_frame = capture.getNextFrame()


# Read and save frames until the user stops the program
while capture.isRunning():

    frame = capture.getNextFrame()

    while frame is None:
        frame = capture.getNextFrame()

    cv2.waitKey(2)

    if prev_frame and frame is not None:
        # Get previous frame in grayscale
        #prev_frame = frame.image

        diff = np.int8(frame.image - prev_frame.image)

        #threshold spatial difference frame
        pos_change = (diff >= change_thresh)*255
        no_change = ((diff > -change_thresh) & (diff < change_thresh))*128
        thresholded_frame = np.zeros(diff.shape)
        thresholded_frame += pos_change
        thresholded_frame += no_change

        sp = thresholded_frame

        frame_count += 1

        cv2.imshow('Frame Output', sp.astype(np.uint8))

        cv2.imwrite(f'./Final_project/Right_Scissors/frame_{frame_count}.jpg', sp.astype(np.uint8))
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    prev_frame = frame
   
        
# Release the webcam
cap.release()

# Close OpenCV windows
cv2.destroyAllWindows()

print(f"{frame_count} frames saved successfully.")