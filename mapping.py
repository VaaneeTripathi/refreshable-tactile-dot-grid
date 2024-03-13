# Program to map the video to an x-y plane 
import numpy as np
import cv2 as cv
from PIL import Image
from video_image_conversion import videoConversion

array = videoConversion('sample.mp4')

def arrayCompression(array_of_frames):
    
    threed_array = []
    
    for frame in range(len(array_of_frames)):
        current_frame = array_of_frames[frame]
        twod_array = []
        for pixel in range(len(current_frame)):
            current_pixel = current_frame[pixel]
            oned_array = []
            # for index in range(len(current_pixel)):
            if (current_pixel == 255).any() == True:
                colour_value = 1
                oned_array.append(colour_value)
            else:
                colour_value = 0
                oned_array.append(colour_value)
            twod_array.append(oned_array)
        threed_array.append(twod_array)

    return threed_array
        
array_to_image = arrayCompression(array)

def testFunction(array1, array2):
    # for i in range(len(array)):
    #     frame = array[i]
    #     array_of_frames = []
    #     for i in range(len(frame)):
    #         pixel = frame[i]
    #         array_of_pixels = []
    #         for i in range(len(pixel)):
    #             if pixel[i] == 1:
    #                 array_of_pixels.append((255, 255, 255))
    #             else:
    #                 array_of_pixels.append((0, 0, 0))
    #     array_of_frames.append(array_of_pixels)
    
    # array = np.array(array_of_frames, dtype=np.uint8)
    # return  array

    a = np.ravel(array1, order = 'K')
    b = np.ravel(array2, order = 'K')


print(len(array))
print(len(array_to_image))


