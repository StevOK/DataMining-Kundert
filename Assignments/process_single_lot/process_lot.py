# Steven Kundert, Jiaxing Liu, Prakriti Pandey
# CMPS 5443 - Data Mining - Griffin
# Assignment 5 - Occupied Parking Space Project
# Part 1 - Image Processing
# 10/2/17

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import json


img = cv.imread('parking1b.jpg')

#plt.imshow(img)
#plt.show()

#img = cv.rectangle(img, (974,1036-974), (491,599-491), (0,255,0), 4)
    
#font = cv.FONT_HERSHEY_SIMPLEX
#cv.putText(img, "This is a rectangle", (230, 50), font, 0.8, (0, 255, 0), 2, cv.LINE_AA)
           

crop_img = img[451:586,701:849]
    

plt.imshow(img)
plt.show()
plt.imshow(crop_img)
plt.show()

hsv = cv.cvtColor(crop_img,cv.COLOR_BGR2HSV)
hist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
np.savetxt('test.out', hist, delimiter=',')

plt.imshow(hist,interpolation = 'nearest')
plt.show()
