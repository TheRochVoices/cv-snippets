import cv2 as cv
import numpy as np

img1 = cv.imread('white.jpg')
img2 = cv.imread('green.jpg')
row, cols, channels = img1.shape
img2 = cv.resize(img2, (cols, row))
#added = white + green
#added1 = cv.add(white, green)
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

# add a threshold
ret, mask = cv.threshold(img2gray, 100, 255, cv.THRESH_BINARY_INV)

mask_inv = cv.bitwise_not(mask)

img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2,img2,mask = mask)

dst = cv.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv.imshow('img1',img1)
#cv.imshow('roi',roi)
#cv.imshow('2gray',img2gray)
cv.imshow('mask',mask_inv)
#cv.imshow('bg',img1_bg)
#cv.imshow('fg',img2_fg)
#cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()
