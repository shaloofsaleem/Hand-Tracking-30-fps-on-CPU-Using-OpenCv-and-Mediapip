import cv2
import mediapipe as mp
import numpy as np
import math
import time


mpHands= mp.solutions.hands
Hands = mpHands.Hands()
mpDraw= mp.solutions.drawing_utils
prevTime= 0


cap = cv2.VideoCapture(0)


while (cap.isOpened()):
    success, img =cap.read()
    cvtImg= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    reslut= Hands.process(cvtImg)
    
    
    if reslut.multi_hand_landmarks:
        for img_in_frame in reslut.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, img_in_frame, mpHands.HAND_CONNECTIONS)
        for Id,lm in enumerate(reslut.reslut.multi_hand_landmarks[0].landmarks):
            h,w,c= img.shape    
            cx,cy= int (lm.x*w),int(lm.y*h)
            lmList
            
    curentTime= time.time()
    fps= 1/(curentTime-prevTime)
    prevTime= curentTime
    
    cv2.putText(img, str(int(fps)), (40,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
            
            
    
    cv2.imshow("Hand Traking", img)
    
    if cv2.waitKey(1)==113: #Q=133
        break
    
    
    