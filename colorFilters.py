import cv2 as cv
import numpy as np

img = cv.imread('power.jpg')


hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV) 
lower_red = np.array([30,150,50])
upper_red = np.array([255,255,180])
mask = cv.inRange(hsv, lower_red, upper_red)
res = cv.bitwise_and(img,img, mask= mask)

cv.imshow('frame', res)
cv.imshow('mask', mask)

cv.waitKey(0)
cv.destroyAllWindows()
