# USAGE
# python index.py --dataset dataset --index index.csv
#cd D:\violettes\Software\Central
#run index.py --dataset D:\violettes\Software\Central\plantes_references\ref_couleurs --index index.csv

# import the necessary packages
from tarax.colordescriptor import ColorDescriptor
import argparse
import glob
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
args = vars(ap.parse_args())

# initialize the color descriptor
cd = ColorDescriptor((8, 12, 3))
#For our image search engine, we’ll be utilizing a 3D color histogram in the HSV color space with 8 bins for the Hue channel, 12 bins for the saturation channel, and 3 bins for the value channel, yielding a total feature vector of dimension 8 x 12 x 3 = 288.
#This means that for every image in our dataset, no matter if the image is 36 x 36 pixels or 2000 x 1800 pixels, all images will be abstractly represented and quantified using only a list of 288 floating point numbers.
# https://www.pyimagesearch.com/2014/12/01/complete-guide-building-image-search-engine-python-opencv/

# open the output index file for writing
output = open(args["index"], "w")

# use glob to grab the image paths and loop over them
#for imagePath in glob.glob(args["dataset"] + "/*.png"):
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):  # Cyril ROUDOT 3 sept 2017
	# extract the image ID (i.e. the unique filename) from the image
	# path and load the image itself
	imageID = imagePath[imagePath.rfind("/") + 1:]
	image = cv2.imread(imagePath)

	# describe the image
	features = cd.describe(image)

	# write the features to file
	features = [str(f) for f in features]
	output.write("%s,%s\n" % (imageID, ",".join(features)))

# close the index file
output.close()