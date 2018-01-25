# cyril 3 sep 2017 :  run .\search.py --index index.csv --query queries/rosette2.jpg --result-path plantes_references

# USAGE
# python search.py --index index.csv --query queries/103100.png --result-path dataset

# import the necessary packages
from tarax.colordescriptor import ColorDescriptor
from tarax.searcher import Searcher
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())

# initialize the image descriptor
cd = ColorDescriptor((8, 12, 3))

# load the query image and describe it
query = cv2.imread(args["query"])
features = cd.describe(query)

# perform the search
searcher = Searcher(args["index"])
results = searcher.search(features)

# display the query

cv2.namedWindow("Query", cv2.WINDOW_NORMAL) 
cv2.resizeWindow("Query", 800, 600)              # Resize window to specified dimensions
cv2.imshow("Query", query)
cv2.waitKey(0)

cv2.namedWindow("Result", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
cv2.resizeWindow("Result", 800, 600)              # Resize window to specified dimensions


# loop over the results
for (score, resultID) in results:
	# load the result image and display it
	#result = cv2.imread(args["result_path"] + "\" + resultID)
	result = cv2.imread(resultID)
	
	cv2.imshow("Result", result)
	cv2.resizeWindow("Result", 800, 600)              # Resize window to specified dimensions
	cv2.waitKey(0)
cv2.destroyAllWindows()