# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 00:17:36 2017

@author: kchaw
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:36:00 2017

@author: kchaw
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 13:18:18 2017

@author: kchaw
"""

# Import the necessary packages
import cv2
import numpy as np
import time
import sys

def sliding_window(image, stepSize, windowSize):
	# slide a window across the image
	for y in range(0, image.shape[0], stepSize):
		for x in range(0, image.shape[1], stepSize):    
			# yield the current window    
			yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])

# Taking input with arguments
image = cv2.imread(sys.argv[1],0)
cv2.imshow("Image",image)

#ret,thresh1 = cv2.threshold(image,0,255,cv2.THRESH_BINARY_INV)
ret,thresh1 = cv2.threshold(image,60,255,cv2.THRESH_BINARY)
cv2.imshow("Thresholded",thresh1)

(winW, winH) = (180, 180)
#max_sum = -sys.maxsize
#max_sum = 15000000
min_sum = 15000000

print("thresh1.shape[0]")
print(thresh1.shape[0])

print("thresh1.shape[1]")
print(thresh1.shape[1])

#for (x,y,window) in sliding_window(thresh1, stepSize=10, windowSize=(winW, winH)):
for x in range(0,439,20):
     for y in range(0,279,20):
        step = 10
        add_pixels = 0
    
   
        for col in range(x+0,x+winH):
            for row in range(y+0,y+winW):
                add_pixels += thresh1[row][col]
    
        
        if min_sum > add_pixels:
            min_col = x
            min_row = y
            min_sum = add_pixels
        
#       print("min_sum",min_sum)
#       print("x",x)
#       print("y",y)
#       print("min_x",min_col)
#       print("min_y",min_row)
        
        # Some classifier
        
        clone = thresh1.copy()
        cv2.rectangle(clone, (x,y), (x + winW, y + winH), (0,0,0), 2)
        cv2.imshow("Window",clone)
        cv2.waitKey(1)
        #time.sleep(0.25)
                   
cv2.waitKey(0)
cv2.destroyAllWindows()
