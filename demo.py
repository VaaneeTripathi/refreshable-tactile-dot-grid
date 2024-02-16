# A program to detect outlines from a captured frame 
import numpy as np 
import cv2 as cv 

# Take the image input
image = cv.imread('test.jpg')
# If the image does not exist, display the same
assert image is not None, "file could not be read, check using os.path.exists()"

# Convert the image to a binary image (with only black and white pixels)
grayscale_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
tvalue, threshold_image = cv.threshold(image, 127, 255, 0)

# Detect the outline
image_out, contours, hierarchy = cv.findContours(threshold_image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# Define a blank white image
blank_image = np.ones((350, 350, 3), dtype = np.uint8)

# Draw contours on image
cv.drawContours(blank_image, contours, -1, (255, 255, 255), 2)

# Display image
cv.imshow("Display", blank_image)
key = cv.waitKey(0)