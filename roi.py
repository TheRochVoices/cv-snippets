import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
	ret, frame = cap.read()
	roi = frame[130:290, 130:290]
	frame[0:160, 0:160] = roi
	cv.imshow('frame', frame)
	if cv.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv.destroyAllWindows()
