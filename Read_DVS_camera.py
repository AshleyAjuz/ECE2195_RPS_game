import dv_processing as dv
import numpy as np
import cv2 as cv
import time

'''
cameras = dv.io.discoverDevices()

print(f"Device discovery: found {len(cameras)} devices.")
for camera_name in cameras:
    print(f"Detected device [{camera_name}]")
'''

# Open camera
capture = dv.io.CameraCapture(cameraName="DAVIS346_00000448")

'''
# Initiate a preview window
cv.namedWindow("Preview", cv.WINDOW_NORMAL)

# Run the loop while camera is still connected
while capture.isRunning():
    # Read a frame from the camera
    frame = capture.getNextFrame()

    # The method does not wait for frame arrive, it returns immediately with
    # latest available frame or if no data is available, returns a `None`
    if frame is not None:
        # Print received packet time range
        print(f"Received a frame at time [{frame.timestamp}]")

        # Show a preview of the image
        cv.imshow("Preview", frame.image)
    cv.waitKey(2)
'''


# Run the loop while camera is still connected
while capture.isRunning():
    # Read a frame from the camera
    frame = capture.getNextFrame()

    # Read batch of events
    events = capture.getNextEventBatch()

    # The method does not wait for data arrive, it returns immediately with
    # latest available data or if no data is available, returns a `None`
    if events is not None and frame is not None:
          # Show a preview of the image
        cv.imshow("Preview", frame.image)

        # Display number of events
        numEvents = np.shape(events)[0]
        print(numEvents)
        cv.putText(frame.image, str(numEvents), (0, 0),
                   cv.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255), 5)


        # Print received packet time range
        #print(f"Received events within time range [{events.getLowestTime()}; {events.getHighestTime()}]")
    cv.waitKey(2)
    '''
    else:
        # No data has arrived yet, short sleep to reduce CPU load
        time.sleep(0.001)
    '''