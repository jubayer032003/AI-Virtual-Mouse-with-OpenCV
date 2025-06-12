import cv2 as cv
import mediapipe as mp
import pyautogui 
import math


# initialize mediapipe and screen size :
mp_hands =mp.solutions.hands
hands = mp_hands.Hands(max_num_hands = 1, min_detection_confidence=0.7) 
mp_draw = mp.solutions.drawing_utils

screen_w , screen_h = pyautogui.size()

# initialize webcam :
cap = cv.VideoCapture(0)

while True :
    success , img = cap.read()
    img = cv.flip(img,1)   
    img_rgb = cv.cvtColor(img , cv.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
            landmark = handLms.landmark

            index_finger = landmark[8] 
            thumb = landmark[4]
            # calculate distance between index finger and thumb
              


              
            distance = math.sqrt((index_finger.x - thumb.x) ** 2 + (index_finger.y - thumb.y) ** 2)
            x = int(index_finger.x * img.shape[1])
            y = int(index_finger.y * img.shape[0])

            #map to screen coordinates
            screen_x = screen_w * index_finger.x
            screen_y = screen_h * index_finger.y
            pyautogui.moveTo(screen_x,screen_y)

            # draw circle on index finger and thumb finger
            cv.circle(img, (x, y), 10, (0, 0, 255), cv.FILLED)
            cv.circle(img, (int(thumb.x * img.shape[1]), int(thumb.y * img.shape[0])), 10, (255, 0,150 ), cv.FILLED)
            
            # calculate distance between index finger and thumb
            # Get thumb coordinates in image
            thumb_x = int(thumb.x * img.shape[1])
            thumb_y = int(thumb.y * img.shape[0])

             # Calculate distance between index finger and thumb
            distance = math.hypot(thumb_x - x, thumb_y - y)

             # If fingers are close, perform a click
            if distance < 40:
                pyautogui.click()
                cv.circle(img, (x, y), 15, (0, 255, 0), cv.FILLED)  # Green circle on click

            
    cv.imshow("Virtual Mouse", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break   
cap.release()
cv.destroyAllWindows()

