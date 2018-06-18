import cv2 as cv
cap = cv.VideoCapture(0)

while True:
	ret, frame = cap.read()
	font = cv.FONT_HERSHEY_SIMPLEX
	cv.putText(frame, 'OpenCV', (10,300), font, 4, (255, 0, 0), 4, cv.LINE_AA)
		# frame, text, position, font, size, color, thickness
	
	cv.rectangle(frame, (384,0), (510,128), (0,255,0), 3)

	cv.imshow('frame', frame)
	if cv.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv.destroyAllWindows()
