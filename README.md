# Dots: A Frugal Refreshable Tactile Dot Grid

A real-time tactile display system that converts live whiteboard content into tactile feedback for visually impaired students. This project aims to bridge the accessibility gap in STEM education by providing an affordable, dynamic alternative to expensive commercial tactile displays.

## Project Overview

Traditional STEM education relies heavily on visual representations—graphs, diagrams, mathematical symbols—creating significant barriers for visually impaired students. Existing commercial tactile displays cost $12,000-$22,500, making them inaccessible to most educational institutions, especially in resource-constrained environments.

The proposed solution provides real-time conversion of instructor whiteboard content into tactile feedback through a 55×75 actuated dot matrix. By targeting a production cost of ~$3,000-$3,500, it aims to make tactile displays accessible to educational institutions while enabling synchronous classroom participation for visually impaired students.

**Key Innovation:** Unlike static tactile graphics that require pre-preparation, this system provides immediate tactile representation of content as it's being written or drawn, allowing visually impaired students to follow along in real-time. Additionally, it opens up the possibility of a 75% cost reduction as compared to currently available market options. 

## System Design

### Architecture Overview
```
Instructor writes on whiteboard → Camera captures content → Raspberry Pi processes images → 
WiFi transmission → STM32 controller → Individual dot actuators create tactile representation
```

### Design Philosophy
- **Frugal Engineering**: Using readily available, cost-effective components
- **Modular Architecture**: Separating image processing from tactile display for scalability
- **Real-time Processing**: Minimal latency between visual input and tactile output
- **Classroom Integration**: Designed to work with existing teaching methods without disruption

### Current Implementation Plan

**Phase 1: Prototype Validation (Current - Work in Progress)**
- Camera (CSI) → Raspberry Pi 4 → USB WiFi → ESP32 → Small dot grid
- Focus on validating core technology and tactile feedback quality

**Phase 2: Full Grid Implementation**
- Same image processing pipeline
- Upgrade to STM32F4 + ESP8266 for controlling 4,125 individual actuators
- Full 55×75 tactile display (A4-sized surface)

**Phase 3: Multi-Unit Classroom Deployment (Future)**
- Multiple tactile displays receiving simultaneous broadcasts
- Enhanced network architecture for classroom-scale deployment

## Inspiration and Core Technology

### Single Actuator Design
Our tactile actuator design is inspired by **Vijay's award-winning Hackaday project** - the "Electromechanical Refreshable Braille Module" from 2023. This innovative approach uses:

- **Miniature electromagnetic solenoids** for actuation force
- **Bistable mechanical cams** that maintain dot position without continuous power
- **3D-printed housing** for compact, manufacturable design

This foundation provides the reliable, low-power actuation mechanism necessary for scaling to thousands of individual dots while keeping costs manageable.

### Hardware Components
- **Image Processing**: Raspberry Pi 4 with Camera Module (CSI interface)
- **Network**: TP-Link AC600 dual-band USB WiFi adapter creating dedicated access point
- **Control**: STM32F4 microcontroller with ESP8266 WiFi module (UART communication)
- **Actuation**: Electromagnetic solenoids with bistable mechanical cams (inspired by Vijay's design)

## Current Implementation Status

```
refreshable-tactile-dot-grid/
├── contour_detection.py       # ✅ Extracts contours from camera input
├── display_frame.py           # ✅ Converts processed frames for display
├── display_video.py           # ✅ Handles video input for processing
├── video_image_conversion.py  # ✅ Converts video into image frames
├── visualisation.py           # ✅ Visualizes processed tactile patterns
├── frame.png                  # Sample frame image
├── image.png                  # Example processed image
├── project.avi                # Sample project video
├── sample.mp4                 # Sample input video
├── .gitignore                 # Git ignore file
└── README.md                  # Project documentation
```

### What's Been Built

**✅ Complete Software Pipeline**
- Real-time image processing using OpenCV
- Contour detection and binary grid mapping (55×75 resolution)
- Visualization tools for testing and validation
- Video processing for development and testing

**✅ Proof-of-Concept Hardware**
- Single tactile actuator prototype based on Vijay's design
- Validated electromagnetic actuation with bistable mechanism
- Confirmed power requirements and mechanical reliability

### Current Development Workflow

1. **Image/Video Capture**: ESP32-CAM or Raspberry Pi Camera captures whiteboard content
2. **Processing Pipeline**: 
   - `video_image_conversion.py` extracts frames from video input
   - `contour_detection.py` identifies key visual elements using OpenCV
   - Binary conversion to 55×75 grid format
3. **Display Preparation**: `display_frame.py` prepares binary data for transmission
4. **Visualization & Testing**: `visualisation.py` allows preview of tactile patterns
5. **Hardware Communication**: Processed data transmitted to microcontroller for actuation

## Technical Specifications

| Component | Current Status | Target Specification |
|-----------|----------------|---------------------|
| **Display Resolution** | Variable (testing) | 55×75 dots (4,125 total) |
| **Refresh Rate** | 5-10 Hz | 10 Hz |
| **Processing Latency** | <200ms | <100ms |
| **Power Requirements** | ~5W (prototype) | ~100W peak (full grid) |
| **Estimated Cost** | ~$225 (5×5 prototype) | ~$3,500 (full system) |

## Next Steps

### Validation of the Concept: Questions to Answer
1. Is synchronous learning more effective?
2. Can the cost be reduced further?
3. How can it be designed to reduce reliance on ideal circumstances?

The next few moths will be best on research, testing, and prototyping to answer these questions before the project moves forward.

### Immediate Development 
1. **Scale to Full Grid**: Build complete 55×75 actuator array
2. **STM32 Integration**: Implement STM32F4 + ESP8266 control system
3. **Power Management**: Optimize multiplexed control for 4,125 actuators
4. **Enclosure Design**: Create ergonomic, durable housing

### User Testing
1. **IRB Approval**: Prepare for human subjects research
2. **Field Testing**: Validate tactile feedback quality with visually impaired users
3. **Educational Assessment**: Measure learning outcomes and classroom integration

### Future Scalability
1. **Multi-Unit Architecture**: Design for classroom deployment
2. **Enhanced Networking**: Implement robust multi-device communication
3. **Cost Optimization**: Explore manufacturing partnerships for volume production

## Contributing

This project welcomes contributions from:
- **Accessibility Researchers**: User experience, educational effectiveness
- **Hardware Engineers**: PCB design, mechanical optimization, manufacturing
- **Software Developers**: Image processing, embedded systems, networking
- **Educators**: Classroom integration, curriculum development

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Links and References

- **Inspiration**: [Vijay's Electromechanical Refreshable Braille Module](https://hackaday.io/project/191181-electromechanical-refreshable-braille-module)
- **Repository**: [GitHub - Refreshable Tactile Dot Grid](https://github.com/VaaneeTripathi/refreshable-tactile-dot-grid)
---

*This project is part of ongoing research in accessible technology for STEM education, supported by Mphasis F1 Foundation and developed at Ashoka University.*
