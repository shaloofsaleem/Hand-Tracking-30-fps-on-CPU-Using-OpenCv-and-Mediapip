import cv2
import mediapipe as mp


cap = cv2.VideoCapture(0)
mpHands= mp.solutions.hands
Hands = mpHands.Hands()
mpDraw= mp.solutions.drawing_utils


while (cap.isOpened()):
    success, img =cap.read()
    cvtImg= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    reslut= Hands.process(cvtImg)
    
    if reslut.multi_hand_landmarks:
        for img_in_frame in reslut.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, img_in_frame, mpHands.HAND_CONNECTIONS)
            
    
    cv2.imshow("Hand Traking", img)
    
    if cv2.waitKey(1)==113: #Q=133
        break
    
    
    