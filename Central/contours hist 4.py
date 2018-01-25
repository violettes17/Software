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
image = cv2.imread(imgloc,0)

#http://docs.opencv.org/3.1.0/d1/db7/tutorial_py_histogram_begins.html
hist = cv2.calcHist([image],[0],None,[256],[0,256])

max_value = max(hist)
from matplotlib import pyplot as plt
plt.hist(image.ravel(),256,[0,256]); plt.show()
#http://www.pyimagesearch.com/2014/01/22/clever-girl-a-guide-to-utilizing-color-histograms-for-computer-vision-and-image-search-engines/

# grab the image channels, initialize the tuple of colors,
# the figure and the flattened feature vector
image = cv2.imread(imgloc)
chans = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
features = []
 
# loop over the image channels
for (chan, color) in zip(chans, colors):
	# create a histogram for the current channel and
	# concatenate the resulting histograms for each
	# channel
	hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
	features.extend(hist)
 
	# plot the histogram
	plt.plot(hist, color = color)
	plt.xlim([0, 256])
 
# here we are simply showing the dimensionality of the
# flattened color histogram 256 bins for each channel
# x 3 channels = 768 total values -- in practice, we would
# normally not use 256 bins for each channel, a choice
# between 32-96 bins are normally used, but this tends
# to be application dependent
import numpy as np
print ('flattened feature vector size: %d' % np.array(features).flatten().shape)


#http://docs.opencv.org/3.1.0/d8/d83/tutorial_py_grabcut.html#gsc.tab=0

#http://www.anser-e.com/AlgorithmEngineering/ComputerVisionAlgorithms.html

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
image = imutils.resize(image, height = 2340)
 
# convert the image to grayscale, blur it, and find edges
# in the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 20, 68, 68)

cv2.namedWindow("output", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
cv2.resizeWindow("output", 1920, 1080) 
#for i in range(1,10) :
edged = cv2.Canny(gray, 0, 28)
cv2.imshow("output", edged)
cv2.waitKey(0)
    
cv2.destroyAllWindows()

# find contours in the edged image, keep only the largest
# ones, and initialize our screen contour
(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#_, contours, _= cv2.findContours(skin_ycrcb, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:71906]
screenCnt = None
perilist=[0]*71906
a=0
# loop over our contours
for c in cnts:
	# approximate the contour
    peri = cv2.arcLength(c, True)
    perilist[a] = cv2.arcLength(c, True)   # perilist[c]= peri
    a = a+1
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    screenCnt = approx
    cv2.drawContours(image, [screenCnt], -1, (0, 0, 0), 3)
    #cv2.drawContours(edged, [screenCnt], -1, (0, 255, 0), 3)
cv2.imshow("Game Boy Screen", image)
cv2.waitKey(0)    

cv2.imshow("output", edged)
cv2.waitKey(0)  
cv2.destroyAllWindows()
	# if our approximated contour has four points, then
	# we can assume that we have found our screen
	#if len(approx) == 4:
		#screenCnt = approx
		#break

