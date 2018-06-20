import cv2 as cv

cap = cv.VideoCapture('test.mp4')

while True:
	ret, img = cap.read()


	cv.imshow('some', img)
	if 0xFF & cv.waitKey(5) == 27:
		break
cv.destroyAllWindows()
