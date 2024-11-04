Here's a simplified, plain text version:

---

# Webcam Object Recognition with ROS and OpenCV

## Overview

This project combines ROS (Robot Operating System) and OpenCV to create a real-time object detection system. Using a webcam, it detects objects like faces in the video feed and visualizes them in RViz, providing a hands-on example of computer vision.

## Prerequisites

Ensure you have the following installed:

- **ROS Noetic** for managing robot nodes and communication.
- **OpenCV** for image processing.
- **Python 3** to run the scripts.
- **cv_bridge** to convert ROS images for OpenCV processing.

## Installation Steps

1. **Create a ROS Workspace:**

   ```bash
   mkdir -p ~/ros_webcam_ws/src
   cd ~/ros_webcam_ws/src
   catkin_init_workspace
   ```

2. **Clone the Project Repository:**

   ```bash
   git clone <repository-url> webcam_object_recognition
   ```

   Replace `<repository-url>` with the URL to the project repository.

3. **Build Your Workspace:**

   ```bash
   cd ~/ros_webcam_ws
   catkin_make
   ```

4. **Source the Workspace:**

   ```bash
   source devel/setup.bash
   ```

## Usage Guide

1. **Start the Object Recognition Node:**

   ```bash
   rosrun webcam_object_recognition webcam_object_recognition.py
   ```

2. **Open RViz:**

   ```bash
   rviz
   ```

3. **Configure RViz:**

   - Add an **Image Display** and set its topic to `/webcam/image_with_detections`.
   - Add a **Marker Display** and set its topic to `/detected_objects`.
   - Ensure the Fixed Frame (e.g., `camera_frame`) is set correctly.

4. **See It in Action**: You should see the webcam feed with detected faces in RViz.

## File Overview

The main script, `webcam_object_recognition.py`, is in the `scripts` directory. It:

- Detects faces using OpenCV’s Haar Cascade classifier.
- Publishes detected objects as markers in RViz.

## Dependencies

Ensure you have these packages:

- `sensor_msgs`, `cv_bridge`, `visualization_msgs`, and `opencv-python`.

To install OpenCV:

```bash
pip install opencv-python
```

## Troubleshooting

- If your webcam doesn’t open, confirm that it’s functioning.
- If RViz isn’t displaying, check that topics are set up correctly and that ROS is sourced.

## License

This project is under the MIT License. See the LICENSE file for details.

## Acknowledgements

Special thanks to the communities behind OpenCV and ROS for their documentation:

- [OpenCV Documentation](https://docs.opencv.org/)
- [ROS Wiki](http://wiki.ros.org/)

---

Thank you for exploring this project! Enjoy learning about robotics and computer vision.
