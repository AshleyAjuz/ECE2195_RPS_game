import aedat
import numpy as np
import cv2 # https://pypi.org/project/opencv-python/

decoder = aedat.Decoder("./Final_project/first_test_video.aedat4")

# Create a blank frame
frame = np.full((260, 346), 128, dtype=np.uint8)

count = 0

for packet in decoder:
    if count == 80:
        # Display the frame
        cv2.imshow("Frame", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        frame = np.full((260, 346), 128, dtype=np.uint8)
        count = 0
    else:
        count+=1
    if "events" in packet:
        for event in packet["events"]:
            if event["on"]:
                # Set the value to 255 at the event coordinates
                frame[event["y"], event["x"]] = 0
            else:
                # Set the value to 255 at the event coordinates
                frame[event["y"], event["x"]] = 255
        

    #frame = cv2.resize(frame, (640, 480))

    


# # Resize frame to fit the screen
# frame = cv2.resize(frame, (640, 480))

# # Display the frame
# cv2.imshow("Frame", frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




'''
index = 0
img = None
for packet in decoder:
    if "frame" in packet:
        image = packet["frame"]["pixels"]
        if packet["frame"]["format"] == "RGB":
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        elif packet["frame"]["format"] == "RGBA":
            image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGRA)  
        img = image          
        index += 1
cv2.imshow("Preview",img)
cv2.waitKey(10)
'''

'''
import os

decoder = aedat.Decoder("./Final_project/first_test_video.aedat4")
print(decoder.id_to_stream())

for packet in decoder:
    print(packet["stream_id"], end=": ")
    if "events" in packet:
        print("{} polarity events".format(len(packet["events"])))
    elif "frame" in packet:
        print("{} x {} frame".format(packet["frame"]["width"], packet["frame"]["height"]))
    elif "imus" in packet:
        print("{} IMU samples".format(len(packet["imus"])))
    elif "triggers" in packet:
        print("{} trigger events".format(len(packet["triggers"])))
'''