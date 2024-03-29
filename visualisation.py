import pygame
import sys
import numpy as np
from display_video import output

# This program takes the output from display_video, draws a grid, and turns relevant cells white to recreate the contours

# Initialize pygame 
pygame.init()

# Constants
WIDTH = len(output[0])
HEIGHT = len(output[0][0])
NO_OF_ROWS = len(output[0])
NO_OF_COLUMNS = len(output[0][0])
DEPTH = len(output)
CELL_SIZE = min(WIDTH // NO_OF_COLUMNS, HEIGHT// NO_OF_ROWS)

# Colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Output Grid")

# Function to draw the grid for a 2D frame
def draw_grid(grid):
    for row in range(NO_OF_ROWS):
        for column in range(NO_OF_COLUMNS):
            x = column * CELL_SIZE
            y = row * CELL_SIZE
            if grid[row][column] == 1:
                pygame.draw.rect(window, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(window, BLACK, (x, y, CELL_SIZE, CELL_SIZE))

running = True
depth_index = 0

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the window
    window.fill(BLACK)

    # Draw the grid for the current 2D slice
    draw_grid(output[depth_index])

    # Update the display
    pygame.display.update()

    # Increment the depth_index/move to next frame and loop back if necessary
    depth_index = (depth_index + 1) % DEPTH

    # Pause for a short duration to control the frame rate
    pygame.time.delay(1)

# Quit pygame
pygame.quit()
sys.exit()
