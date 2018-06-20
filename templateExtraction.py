import cv2 
import numpy as np


image = cv2.imread('in.jpg')
imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template = cv2.imread('to.jpg', 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(imgGray,template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
	print(pt)

for pt in zip(*loc[::-1]):
	
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.imshow('Detected',image)

cv2.waitKey(0)


'''[101, 101, 102, 102, 102, 103, 103, 151, 151, 151, 152, 152, 152, 153, 153, 153, 199, 200, 200, 201, 201, 246]), 
   [545, 546, 545, 546, 547, 545, 546, 543, 544, 545, 543, 544, 545, 543, 544, 545, 541, 540, 541, 540, 541, 538]))
'''
