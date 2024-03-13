# Program to convert video stream to images and process them 
import cv2 as cv 
from contour_detection import contour_detection
import glob

def videoConversion(filename):

    # Take a videostream, output images 
    video = cv.VideoCapture(filename)
    
    # Get the number of frames
    no_of_frames = video.get(cv.CAP_PROP_FRAME_COUNT)

    # Initialize an empty array to store frames
    array_of_frames = []

    # Detect contours in each frame and append to array
    for frame_id in range(int(no_of_frames)):
   
        # Extract the frame from the video
        video.set(cv.CAP_PROP_POS_FRAMES, frame_id)
        ret, frame = video.read()
        cv.imwrite('frame.png', frame)
        result = contour_detection('frame.png')
        array_of_frames.append(result)
    
    out = cv.VideoWriter('project.avi',cv.VideoWriter_fourcc(*'XVID'), 15, (500, 500))

    for img in range(len(array_of_frames)):
        out.write(array_of_frames[img])
    out.release()
    return array_of_frames

# with open("output1.txt", "w") as f:
#     f.write(videoConversion("sample.mp4"))

