import numpy as np
import cv2

cap = cv2.VideoCapture('/Users/StarShipIV/Google_Drive/Progetti/Contatore_Uova/Dati/White_Eggs_Conveyor.mov')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

cap = cv2.VideoCapture('/Users/StarShipIV/Google_Drive/Progetti/Contatore_Uova/Dati/White_Eggs_Conveyor.mov')

ret1, frame1 = cap.read(1)
ret2, frame2 = cap.read(100)