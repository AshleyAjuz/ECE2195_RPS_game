import numpy as np
import cv2
import mediapipe as mp
import dv_processing as dv
from RPS_gameplay import RPS

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Open camera
capture = dv.io.CameraCapture(cameraName="DAVIS346_00000448")

# Define the threshold values
PIX_OFF_THRESH = -10
PIX_ON_THRESH = 10

# Function to determine if an event is positive, negative, or neutral
def threshold(diff):
   # If above threshold: positive (WHITE)
   if diff >= PIX_ON_THRESH:
       return 255
   # If below threshold: negative (BLACK)
   elif diff <= PIX_OFF_THRESH:
       return 0
   else:
       # Otherwise: neutral (GRAY)
       return 128

def find_finger_positions(handedness, landmarks):
    finger_positions = [0, 0, 0, 0, 0] # pointing indwards: 0, outwards: 1
    fingers = [4, 8, 12, 16, 20] # Tip finger indices
    for i, finger in enumerate(fingers):
        if finger != 4: # If not thumb
            if landmarks[finger].y < landmarks[finger-1].y:
                finger_positions[i] = 1
            else:
                finger_positions[i] = 0
        elif finger == 4: # If thumb
            if handedness == 'Left':
                if landmarks[finger].x > landmarks[3].x:
                    finger_positions[i] = 1
                else:
                    finger_positions[i] = 0
            elif handedness == 'Right':
                if landmarks[finger].x < landmarks[finger+1].x:
                     finger_positions[i] = 1
                else:
                    finger_positions[i] = 0

    return finger_positions



# Vectorize function to avoid for-loops
# Can be applied to whole matrix in this case!
vecfunc = np.vectorize(threshold)

# Open Webcam 
#cap = cv2.VideoCapture(0)

# Continuously grab one frame at a time using a while loop
# Until an exit command is pressed
#ret, frame = cap.read()


while capture.isRunning():
   frame = capture.getNextFrame()

   if frame is not None:
    # Get previous frame in grayscale
    prev_frame = frame.image

    # Get current frame
    #ret, frame = cap.read()
    frame = capture.getNextFrame()

    if frame is not None:
        # Translate current frame into grayscale
        gray = frame.image
        
        # Get the difference matrix between the two frames
        # Ensure it is in SIGNED int form (negative values allowed)
        diff = np.int8(prev_frame - gray)
        
        # Apply thresholding function to matrix
        disp = vecfunc(diff)

        # Now, display the thresholded difference matrix
        disp = disp.astype(np.uint8)
        
        # get hand locations
        res=mp_hands.Hands().process(frame.image.real)
        multi_handedness = res.multi_handedness
        multi_hand_landmarks = res.multi_hand_landmarks

        # Counting the fingers
        finger_up = 0
        if multi_handedness != None or multi_hand_landmarks != None:
            for classification, hand_landmarks in zip(multi_handedness, multi_hand_landmarks):
                finger_positions = find_finger_positions(classification.classification[0].label,
                hand_landmarks.landmark)
                finger_up += sum(finger_positions)

                #print(finger_up)

        cv2.imshow(f"Threshold: +/- {PIX_ON_THRESH}", disp)
        
        # Wait for 1ms before getting the next frame
        # Will also direct code to break out of the loop if exit key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            #print(finger_up)
            RPS(finger_up)
            break
        
        # Assign previous frame to current frame
        prev_frame = frame
   

