# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 21:58:39 2017

@author: Cyril ROUDOT
"""
#context  windows10 / anaconda / python 3.2.0
import cv2
print(cv2.__version__) # 3.2.0
#imgloc = "D:/violettes/Software/Central/test.jpg" #this path works fine.  
# imgloc = "D:\\violettes\\Software\\Central\\test.jpg"   this path works fine also. 
#imgloc = "D:\violettes\Software\Central\test.jpg" #this path fails.
#imgloc = "D:/violettes/Software/Central/IMG_7006.JPG"
imgloc = "D:/violettes/Software/Central/IMG_20170521_171632202.jpg"
image = cv2.imread(imgloc)
height, width, channels = image.shape
print (height, width, channels)

cv2.namedWindow("output", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
cv2.resizeWindow("output", 400, 300)              # Resize window to specified dimensions


cv2.imshow("output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


import imutils
ratio = image.shape[0] / 300.0
orig = image.copy()
image = imutils.resize(image, height = 300)
 
# convert the image to grayscale, blur it, and find edges
# in the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 30, 200)

cv2.namedWindow("output", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
cv2.resizeWindow("output", 400, 300)              # Resize window to specified dimensions


cv2.imshow("output", edged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# find contours in the edged image, keep only the largest
# ones, and initialize our screen contour
(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#_, contours, _= cv2.findContours(skin_ycrcb, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
screenCnt = None
perilist=[0]*100
a=0
# loop over our contours
for c in cnts:
	# approximate the contour
    peri = cv2.arcLength(c, True)
    perilist[a] = cv2.arcLength(c, True)   # perilist[c]= peri
    a = a+1
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    screenCnt = approx
    cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
    cv2.drawContours(edged, [screenCnt], -1, (0, 255, 0), 3)
cv2.imshow("Game Boy Screen", image)
cv2.waitKey(0)    

cv2.imshow("output", edged)
cv2.waitKey(0)  
 
	# if our approximated contour has four points, then
	# we can assume that we have found our screen
	#if len(approx) == 4:
		#screenCnt = approx
		#break

