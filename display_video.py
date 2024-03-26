from display_frame import displayFrame
from video_image_conversion import videoConversion
import ctypes

array = videoConversion('Recording 2024-03-26 204647.mp4')

def displayVideo(array_of_frames):
    video_array = []
    for frame in array_of_frames:
        frame_array = displayFrame(frame)
        video_array.append(frame_array)
    
    return video_array


# def python_to_c(python_array):
#       c_array_type = ctypes.c_int * len(python_array)
#       c_array = c_array_type(python_array)
#       return c_array


# c_array = python_to_c(arrayCompression(array))

# array_pointer = ctypes.cast(array_to_single_frame(array_to_image), ctypes.POINTER(ctypes.c_int))

print(displayVideo(array))