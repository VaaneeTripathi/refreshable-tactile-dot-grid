# This programe take a frame and displays it to the led
import numpy as np
import cv2 as cv
from contour_detection import contour_detection


def displayFrame(frame_array):
    for row in frame_array:
        for pixel in range(len(row)):
            # print(f"{pixel = }")
            if row[pixel] == 255:
                row[pixel] = 1

    return frame_array

# frame = contour_detection("frame.png")
# print(displayFrame(frame))













