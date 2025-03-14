# Refreshable Tactile Dot Grid

## Project Structure
```
refreshable-tactile-dot-grid/
├── contour_detection.py       # Extracts contours from camera input
├── display_frame.py           # Converts processed frames for display
├── display_video.py           # Handles video input for processing
├── video_image_conversion.py  # Converts video into image frames
├── visualisation.py           # Visualizes processed tactile patterns
├── frame.png                  # Sample frame image
├── image.png                  # Example processed image
├── project.avi                # Sample project video
├── sample.mp4                 # Sample input video
├── .gitignore                 # Git ignore file
└── README.md                  # Project documentation
```

## Workflow
The project follows a structured workflow to process visual data and convert it into a tactile representation:

1. **Image/Video Capture**:
   - The ESP32-CAM captures real-time images or videos.
   - Alternatively, pre-recorded videos can be used as input.

2. **Preprocessing**:
   - `video_image_conversion.py` extracts frames from video input.
   - `contour_detection.py` processes these frames to identify key contours using OpenCV.

3. **Binary Representation**:
   - The extracted contours are converted into a binary dot-matrix format.
   - `display_frame.py` takes this binary representation and prepares it for display.

4. **Tactile Display Actuation**:
   - The STM32 microcontroller receives the processed data.
   - The electromagnet-based dot grid is actuated accordingly, forming the tactile representation.

5. **Visualization & Testing**:
   - `visualisation.py` is used to preview the processed tactile patterns before actuation.
   - `display_video.py` can be used to simulate the real-time processing of moving content.

## Setup & Installation
### Prerequisites
- Python 3.8+
- OpenCV
- NumPy
- ESP32-CAM for image capture
- Raspberry Pi 4 for processing
- STM32 microcontroller for actuation

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/refreshable-tactile-dot-grid.git
   cd refreshable-tactile-dot-grid
   ```
2. Install dependencies:
   ```bash
   pip install opencv-python numpy
   ```
3. Run the contour detection module:
   ```bash
   python contour_detection.py
   ```
4. Process and display a sample frame:
   ```bash
   python display_frame.py
   ```


## Contributing
Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request.

## License
This project is licensed under the MIT License.

