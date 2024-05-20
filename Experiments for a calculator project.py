# هاذا كود يعمل على تسجيل شاشة الهدف(يوجد خطء)
#import pyautogui
#import cv2
#import time
#import numpy as np
#print("All libraries imported successfully!")
# Screen recording settings
#SCREEN_SIZE = (1920, 1080)  # Adjust based on your screen resolution
#VIDEO_NAME = "screen_recording.mp4"
#FPS = 30
#RECORDING_TIME = 10000  # Duration of the recording in seconds
#________________________________________________________________________________
#def record_screen():
#    print("Recording started!")

    # Start screen recording
#    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#    out = cv2.VideoWriter(VIDEO_NAME, fourcc, FPS, SCREEN_SIZE)
#    start_time = time.time()

#    while (time.time() - start_time) < RECORDING_TIME:
        # Capture screen
#        screenshot = pyautogui.screenshot()
 #       frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Write frame to video file
#        out.write(frame)

    # Release video writer
#    out.release()

#    print("Recording finished! Saved as", VIDEO_NAME)

# Call the function to start recording
#record_screen()







# هاذا الكود يعمل على تسجيل شاشة الهدف يعمل بشكل سليم

import pyautogui
import cv2
import time
import numpy as np
import os

print("All libraries imported successfully!")

# Print current working directory
print(f"Current working directory: {os.getcwd()}")

# Screen recording settings
SCREEN_SIZE = pyautogui.size()  # Automatically detect screen resolution
VIDEO_NAME = "screen_recording.mp4"
FPS = 3              # عدد الفريمات وا سرعة التشغيل
RECORDING_TIME = 10  # Duration of the recording in seconds for testing purposes

def record_screen():
    print("Recording started!")

    # Start screen recording
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    try:
        out = cv2.VideoWriter(VIDEO_NAME, fourcc, FPS, (SCREEN_SIZE.width, SCREEN_SIZE.height))
        start_time = time.time()

        while (time.time() - start_time) < RECORDING_TIME:
            # Capture screen
            screenshot = pyautogui.screenshot()
            frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

            # Write frame to video file
            out.write(frame)

            # Print debug information
            print(f"Recording frame at time: {time.time() - start_time:.1f} seconds")

            # Ensure the recording matches the FPS
            time.sleep(1 / FPS)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Release video writer
        if out is not None:
            out.release()
        print("Recording finished! Saved as", VIDEO_NAME)

# Call the function to start recording
record_screen()















