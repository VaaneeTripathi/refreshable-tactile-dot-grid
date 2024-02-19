# Program to convert video stream to images and process them 
import cv2 as cv 
import contour_detection

def main(filename):

    # Take a videostream, output images 
    video = cv.VideoCapture(filename)
    
    # Get the number of frames
    no_of_frames = video.get(cv.CAP_PROP_FRAME_COUNT)

    for frame_id in range(no_of_frames):
   
        # Extract the frame from the video
        video.set(cv.CAP_PROP_POS_FRAME, frame_id)
        ret, frame = video.read()
        contour_detection(frame)


