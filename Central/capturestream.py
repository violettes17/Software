# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 12:29:23 2018

@author: Cyril
"""
import numpy as np
import cv2
cam = cv2.VideoCapture('http://192.168.1.23:8080/?action=stream')
lower_green = np.array ([55,0,0])
upper_green = np.array ([65,255,255])

lower_yellow = np.array ([16,0,0])
upper_yellow = np.array ([21,255,255])


lower_black = np.array ([0,0,0])
upper_black = np.array ([255,255,40])

# grab the dimensions and compute the center of the image
ret,image = cam.read()
(h, w) = image.shape[:2]
(cX, cY) = (int(w*0.95 ), int(h))


  # touche k=38 fleche du haut
  # touche k=40 fleche du bas
seuil = 10

while True : 
    ret,image = cam.read()
    if ret == True :
        
        (axesX, axesY) = (int(h *0.95  ), int(h *0.95  ))
        ellipMask = np.zeros(image.shape[:2], dtype = "uint8")
        cv2.ellipse(ellipMask, (cX, cY), (axesX, axesY), 0, 0, 360, 255, -1, lineType = 8, shift = 1)#cyril 05 aout 2017
        
        #ellipMask= cv2.bitwise_not(ellipMask)  # mask pour eliminer l'exterieur du fish-eye
               
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        
        res = cv2.bitwise_and(image, image, mask = ellipMask)  #conservation uniquement de l'interieur de l'objectif 
        # ça fonctionne maintenant il faudra utiliser le mask ellipmask en inverse pour aller chercher le tire bouchon noir.
        
        mask = cv2.inRange(hsv,lower_black, upper_black)# lower_black, upper_black)
        
        
        #mask = cv2.subtract(mask, ellipMask)
        mask_inv= cv2.bitwise_not(mask)
    
        
        
        kernel = np.ones((40,40),np.uint8)
        erosion = cv2.erode(mask, kernel, iterations = 1)
        # dilation = cv2.dilate(mask, kernel, iterations = 1)              ne donne rien
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        # closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)    ne donne rien
        
        opening_inv= cv2.bitwise_not(opening)
        res2 = cv2.bitwise_and(image, image, mask = opening)
        
        cv2.imshow('ground',res)
    
    k = cv2.waitKey(5) & 0xFF
    if k ==27 :
        break
    elif k == 38 :
        seuil=seuil+10
        print (seuil)
    elif k== 40 :
        seuil=seuil-10
        print(seuil)
    
    #elif k==-1:  # normally -1 returned,so don't print it
     #   continue
    #else:
       # print (k) # else print its value


cv2.destroyAllWindows()
cam.release();
