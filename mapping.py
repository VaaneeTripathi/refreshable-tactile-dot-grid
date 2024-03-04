# Program to map the video to an x-y plane 
import numpy as np
import cv2 as cv
from video_image_conversion import videoConversion

array = videoConversion('SAMPLE.mp4')

def arrayCompression(array_of_frames):
    
    threed_array = []
    
    for frame in range(len(array_of_frames)):
        current_frame = array_of_frames[frame]
        twod_array = []
        for pixel in range(len(current_frame)):
            current_pixel = current_frame[pixel]
            oned_array = []
            for index in range(len(current_pixel)):
                if current_pixel[index] == 255:
                    colour_value = 1
                    oned_array.append(colour_value)
                else:
                    colour_value = 0
                    oned_array.append(colour_value)
            twod_array.append(oned_array)
        threed_array.append(twod_array)

    return threed_array
        
print(arrayCompression(array))