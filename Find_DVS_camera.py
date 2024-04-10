import dv_processing as dv


cameras = dv.io.discoverDevices()

print(f"Device discovery: found {len(cameras)} devices.")
for camera_name in cameras:
    print(f"Detected device [{camera_name}]")

capture = dv.io.CameraCapture(cameraName="DAVIS346_00000448")

# Print the camera name
print(f"Opened [{capture.getCameraName()}] camera, it provides:")

# Check whether event stream is available
if capture.isEventStreamAvailable():
    # Get the event stream resolution
    resolution = capture.getEventResolution()

    # Print the event stream capability with resolution value
    print(f"* Frames at ({resolution}) resolution")

# Check whether frame stream is available
if capture.isFrameStreamAvailable():
    # Get the frame stream resolution
    resolution = capture.getFrameResolution()

    # Print the frame stream capability with resolution value
    print(f"* Frames at ({resolution}) resolution")

# Check whether the IMU stream is available
if capture.isImuStreamAvailable():
    # Print the imu data stream capability
    print("* IMU measurements")

# Check whether the trigger stream is available
if capture.isTriggerStreamAvailable():
    # Print the trigger stream capability
    print("* Triggers")