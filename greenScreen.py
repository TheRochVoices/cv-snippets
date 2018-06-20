import cv2 as cv
import numpy as np
cap = cv.VideoCapture('test.mp4')
img = cv.imread('house.jpg')
while True:
	ret, img = cap.read()
	hued = cv.cvtColor(img, cv.COLOR_BGR2HSV)
	lower = np.array([0,0,0])
	upper = np.array([255,255,0])
	mask = cv.inRange(hued, lower, upper)
	mask = cv.bitwise_not(mask)
	#res = img + mask
	#not done
	cv.imshow('some', res)
	if 0xFF & cv.waitKey(5) == 27:
		break
cv.destroyAllWindows()
