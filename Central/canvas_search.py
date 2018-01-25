# cyril 21 dec 2017 :  run .\canvas_search.py --index index.csv --query queries/file:///D:/violettes/Software/Central/deux_rosettes_gazon_fin.jpg --result-path plantes_references/ref_couleurs


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


# grab the dimensions and compute the center of the image
(h, w) = query.shape[:2]

#les segments sont décrits par des rectangles   (x_i, x_j, y_i, y_j)  et  i et j sont les coins supérieur-haut et inférieur-bas
segments = []
segments_results = []
divisionW = 10
divisionH = 10

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
    crop_img = query[startY:endY, startX:endX]
    features = cd.describe(crop_img)
    # perform the search
    searcher = Searcher(args["index"])
    results = searcher.search(features)
    segments_results.append(results)

    # display the query

    cv2.namedWindow("Query", cv2.WINDOW_NORMAL) 
    cv2.resizeWindow("Query", 800, 600)              # Resize window to specified dimensions
    cv2.imshow("Query", crop_img)
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