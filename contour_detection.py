# A program to detect outlines from a captured frame 
import numpy as np 
import cv2 as cv 

def contour_detection(filename):
    """Detects contours from an image and draws the contours on a blank image

    Args:
        filename (image): image whose contours are to be detected

    Returns:
        image: image with drawed contours, an array of arrays (no. of rows) and with elements equal to number of elements
    """

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
    blank_image = np.zeros((900, 900), dtype = np.uint8)

    # Draw contours on image
    cv.drawContours(blank_image, contours, -1, (255, 255, 255), 2)

    # Display image
    # cv.imshow("Display", blank_image)
    # result = cv.imwrite('image.png', blank_image)
    # cv.waitKey(1000//60)
    return blank_image

