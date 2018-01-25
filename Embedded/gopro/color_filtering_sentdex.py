# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 09:53:08 2017

@author: Cyril
"""

import cv2
import numpy as np


imgloc = "D:/violettes/Software/Central/deux_rosettes_gazon_fin.jpg"
#imgloc = "D:/violettes/Software/Central/sainSmart_good11_32220_11.jpg"

image = cv2.imread(imgloc)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

while True:
    # hsv hue sat value
    #lower_red = np.array ([100,150,50])
    #upper_red = np.array ([180,255,255])
    lower_green = np.array ([55,0,0])
    upper_green = np.array ([65,255,255])
    
    mask = cv2.inRange(hsv, lower_green, upper_green)
    res = cv2.bitwise_and(image, image, mask = mask)
    
    kernel = np.ones((40,40),np.uint8)
    
    
    #res2 = cv2.morphologyEx(res,cv2.MORPH_OPEN, kernel)
    
    erosion = cv2.erode(mask, kernel, iterations = 1)
   # dilation = cv2.dilate(mask, kernel, iterations = 1)              ne donne rien
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
   # closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)    ne donne rien
    res2 = cv2.bitwise_and(image, image, mask = opening)
    
    
    
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    sobelx = cv2.Sobel(image,cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(image,cv2.CV_64F, 0, 1, ksize=7)
    edges = cv2.Canny(image,400,400)
    
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
    cv2.resizeWindow("image", 1920, 1080) 
    cv2.namedWindow("mask", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
    cv2.resizeWindow("mask", 1920, 1080) 
    cv2.namedWindow("res", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
    cv2.resizeWindow("res", 1920, 1080) 
    cv2.namedWindow("res2", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
    cv2.resizeWindow("res2", 1920, 1080) 
    cv2.namedWindow("erosion", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
    cv2.resizeWindow("erosion", 1920, 1080) 
    cv2.namedWindow("opening", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
    cv2.resizeWindow("opening", 1920, 1080) 
    cv2.namedWindow("laplacian", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
    cv2.resizeWindow("laplacian", 1920, 1080) 
    cv2.namedWindow("sobelx", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
    cv2.resizeWindow("sobelx", 1920, 1080) 
    cv2.namedWindow("sobely", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
    cv2.resizeWindow("sobely", 1920, 1080) 
    cv2.namedWindow("edges", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
    cv2.resizeWindow("edges", 1920, 1080) 
    
    cv2.imshow('image', image)
    
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('res2', res2)
    cv2.imshow('erosion', erosion)
    cv2.imshow('opening', opening)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('edges', edges)
    
    k=cv2.waitKey(5) & 0xFF
    if k==27 :   break   # touche echap
    

cv2.destroyAllWindows()


# convertir une couleur BGR en HSV
green = np.uint8([[[13,82,15]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print (hsv_green)

# travail sur les histogrammes pour localiser les couleurs dominantes

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
import pylab as plb
from scipy.optimize import curve_fit
from scipy import asarray as ar,exp

#https://docs.opencv.org/3.3.1/dd/d0d/tutorial_py_2d_histogram.html
#realisation d'un tableau de 180 teintes et 256 saturation
hist1 = cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])   #tableau teinte saturation
hist2 = cv2.calcHist([hsv],[0,2],None,[180,256],[0,180,0,256])   #tableau teinte valeur

type(hist1)

len(hist2[:,0])


histTeinte = []    #somme des Saturations pour chacune des teintes
for teinte in  range(0,180,1) :     
    histTeinte.append(sum(hist1[teinte])) 
len (histTeinte)

histSaturation = []   #somme des teintes pour chacune des Saturation
for Saturation in  range(0,256,1) :     
    histSaturation.append(sum(hist1[:,Saturation])) 

histValeur = []   #somme des teintes pour chacune des Valeurs
for Valeur in  range(0,256,1) :     
    histValeur.append(sum(hist2[:,Valeur])) 




norm_teinte = normalize(histTeinte).ravel()
norm_Saturation = normalize(histSaturation).ravel()
norm_Valeur = normalize(histValeur).ravel()


#tentative d'approx de la saturation par une gaussienne, boffff
x_teinte = ar(range(len (norm_teinte)))
x = ar(range(len (norm_Saturation)))
y = ar(norm_Saturation)

n = len(x)                          #the number of data
mean = sum(x*y)/n                   #note this correction
sigma = sum(y*(x-mean)**2)/n        #note this correction

np.argmax(y)

def gaus(x,a,x0,sigma):
    return a*exp(-(x-x0)**2/(2*sigma**2))

popt,pcov = curve_fit(gaus,x,y,p0=[1,mean,sigma])

# Two subplots, unpack the axes array immediately
f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True)
ax1.plot(x_teinte,norm_teinte,'b+:',label='data')
ax2.plot(x,norm_Saturation,'b+:',label='data')
ax3.plot(x,norm_Valeur,'b+:',label='data')
ax2.plot(x,gaus(x,*popt),'ro:',label='fit')
plt.legend()
ax1.set_title('teinte')
ax2.set_title('saturation')
ax3.set_title('valeur')
plt.show()

# the histogram of the data
#n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)
#plt.plot(norm_teinte)  #, 50, normed=1, facecolor='green', alpha=0.75)
plt.plot(norm_Saturation)  #, 50, normed=1, facecolor='green', alpha=0.75)

# add a 'best fit' line
#y = mlab.normpdf( bins, mu, sigma)
#l = plt.plot( norm_teinte, 'r--', linewidth=1)

plt.xlabel('Teinte/Saturation')
plt.ylabel('Probability')
#plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
#plt.axis([0, 180, 0, 1])
plt.grid(True)

plt.show()


# Two subplots, unpack the axes array immediately
f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)











