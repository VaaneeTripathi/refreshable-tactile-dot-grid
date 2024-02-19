# A program to detect outlines from a captured frame 
import numpy as np 
import cv2 as cv 

def contour_detection(filename):

    # Take the image input
    image = cv.imread(filename)
    
    # If the image does not exist, display the same
    assert image is not None, "file could not be read, check using os.path.exists()"

    # Convert the image to a binary image (with only black and white pixels)
    grayscale_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    tvalue, threshold_image = cv.threshold(grayscale_image, 127 , 255, 0)

    # Detect the outline
    contours, hierarchy = cv.findContours(threshold_image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Define a blank white image
    blank_image = np.zeros((2500, 2500, 3), dtype = np.uint8)

    # Draw contours on image
    cv.drawContours(blank_image, contours, -1, (0, 0, 255), 2)

    # Display image
    cv.imshow("Display", blank_image)
    key = cv.waitKey(0)