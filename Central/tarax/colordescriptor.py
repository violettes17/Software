# import the necessary packages
import numpy as np
import cv2

class ColorDescriptor:
    def __init__(self, bins):
		# store the number of bins for the 3D histogram
        self.bins = bins

    def describe(self, image):
		# convert the image to the HSV color space and initialize
		# the features used to quantify the image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        features = []

		# grab the dimensions and compute the center of the image
        (h, w) = image.shape[:2]

      #les segments sont décrits par des rectangles   (x_i, x_j, y_i, y_j)  et  i et j sont les coins supérieur-haut et inférieur-bas
        segments = []
        divisionW = 4
        divisionH = 4

        w_segment = int(w/divisionW)
        h_segment = int(h/divisionH)

        for tickH in range(0,divisionH,1) :          #ligne suivante
            y_i = tickH *h_segment
            y_j =  y_i + h_segment
            for tickW in range(0,divisionW,1) :          #colonne suivante
                x_i = tickW*w_segment
                x_j = x_i + w_segment
                segments.append((x_i, x_j, y_i,y_j))  

		# loop over the segments

        for (startX, endX, startY, endY) in segments:
			# construct a mask for each corner of the image, subtracting
            cornerMask = np.zeros(image.shape[:2], dtype = "uint8")
            cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)

			# extract a color histogram from the image, then update the
			# feature vector
            hist = self.histogram(image, cornerMask)
            features.extend(hist)

		# return the feature vector
        return features

    def histogram(self, image, mask):
		# extract a 3D color histogram from the masked region of the
		# image, using the supplied number of bins per channel; then
		# normalize the histogram
        hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins,
			[0, 180, 0, 256, 0, 256])
        hist = cv2.normalize(hist,hist).flatten()  # (hist,hist) ald (hist) cyril et juliette 2 septembre 2017
		# return the histogram
        return hist