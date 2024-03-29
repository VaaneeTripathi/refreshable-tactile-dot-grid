from display_frame import displayFrame
from video_image_conversion import videoConversion

array = videoConversion('sample.mp4')

def displayVideo(array_of_frames):
    video_array = []
    for frame in array_of_frames:
        frame_array = displayFrame(frame)
        video_array.append(frame_array)
    
    return video_array

output = displayVideo(array)