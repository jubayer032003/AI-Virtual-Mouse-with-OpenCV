#AI Virtual Mouse using OpenCV, MediaPipe & PyAutoGUI

This project creates a virtual AI-powered mouse controlled by your hand gestures using your webcam! It tracks your index finger to move the cursor and clicks when your index finger and thumb touch.

## Features
- Cursor control using hand movements
- Click detection (index finger + thumb pinch)
- Real-time hand tracking
- Built with OpenCV, MediaPipe, and PyAutoGUI

## How it Works
1. Captures live video feed from your webcam.
2. Uses MediaPipe to detect hand landmarks.
3. Maps index finger position to screen coordinates.
4. Moves mouse using PyAutoGUI.
5. If index finger and thumb come close → triggers a click.

##Technologies Used
- Python
- OpenCV (`cv2`)
- MediaPipe (Hand Tracking)
- PyAutoGUI (for controlling the mouse)

## ✅ Requirements
- Python 3.7 – 3.10 (MediaPipe doesn't support 3.13+ yet)
- Libraries:
  ```bash
  pip install opencv-python mediapipe pyautogui
