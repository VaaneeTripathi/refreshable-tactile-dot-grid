# Program to convert video stream to images and process them 
import cv2 as cv 
from contour_detection import contour_detection

def main(filename):

    # Take a videostream, output images 
    video = cv.VideoCapture(filename)
    
    # Get the number of frames
    no_of_frames = video.get(cv.CAP_PROP_FRAME_COUNT)

    for frame_id in range(int(no_of_frames)):
   
        # Extract the frame from the video
        video.set(cv.CAP_PROP_POS_FRAMES, frame_id)
        ret, frame = video.read()
        cv.imwrite('frame.png', frame)
        contour_detection('frame.png')


main('SAMPLE.mp4')