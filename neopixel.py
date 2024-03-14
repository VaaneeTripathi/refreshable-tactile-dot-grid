# Program to control LED neopixels 
import board
import neopixel
from mapping import array_to_image

pixels = neopixel.NeoPixel(board.D18, 25)

for index in pixels:
    colour_id = array_to_image[index]
    if colour_id == 1:
        pixels[index] = (255, 255, 255)