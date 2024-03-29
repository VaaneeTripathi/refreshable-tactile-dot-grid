from display_frame import displayFrame
from video_image_conversion import videoConversion

array = videoConversion('sample.mp4')

def displayVideo(array_of_frames):
    """Calls function displayFrame for each frame in a video

    Args:
        array_of_frames (array): 3D array of all frames in a video

    Returns:
        array: simplified 3D array
    """
    video_array = []
    for frame in array_of_frames:
        frame_array = displayFrame(frame)
        video_array.append(frame_array)
    
    return video_array

output = displayVideo(array)