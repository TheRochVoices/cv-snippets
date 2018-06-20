import cv2 as cv
import numpy as np

img = cv.imread('bookpage.jpg')
#ret, treshed = cv.threshold(img, 12, 255, cv.THRESH_BINARY)
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#ret, treshed = cv.threshold(imgGray, 12, 255, cv.THRESH_BINARY)
adapt = cv.adaptiveThreshold(imgGray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 115, 1)
cv.imshow('page', img)
cv.imshow('tresh', adapt)
cv.imshow('gray', imgGray)

cv.waitKey(0)
cv.destroyAllWindows()	
