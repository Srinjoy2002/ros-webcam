Webcam Object Recognition with ROS and OpenCV
=============================================

Overview

This project combines ROS (Robot Operating System) and OpenCV to create a real-time object detection system. Using a webcam, it detects objects like faces in the video feed and visualizes them in RViz, providing a hands-on example of computer vision.

Prerequisites

Ensure you have the following installed:

*   ROS Noetic for managing robot nodes and communication.
    
*   OpenCV for image processing.
    
*   Python 3 to run the scripts.
    
*   cv\_bridge to convert ROS images for OpenCV processing.
    

Installation Steps

1.  mkdir -p ~/ros\_webcam\_ws/srccd ~/ros\_webcam\_ws/srccatkin\_init\_workspace
    
2.  git clone webcam\_object\_recognitionReplace with the URL to the project repository.
    
3.  cd ~/ros\_webcam\_wscatkin\_make
    
4.  source devel/setup.bash
    

Usage Guide

1.  rosrun webcam\_object\_recognition webcam\_object\_recognition.py
    
2.  rviz
    
3.  Configure RViz
    
    *   Add an Image Display and set its topic to /webcam/image\_with\_detections.
        
    *   Add a Marker Display and set its topic to /detected\_objects.
        
    *   Ensure the Fixed Frame (e.g., camera\_frame) is set correctly.
        
4.  See It in Action - You should see the webcam feed with detected faces in RViz.
    

File Overview

The main script, webcam\_object\_recognition.py, is in the scripts directory. It:

*   Detects faces using OpenCV’s Haar Cascade classifier.
    
*   Publishes detected objects as markers in RViz.
    

Dependencies

Ensure you have these packages:

*   sensor\_msgs, cv\_bridge, visualization\_msgs, and opencv-python.
    

To install OpenCV:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install opencv-python   `

Troubleshooting

*   If your webcam doesn’t open, confirm that it’s functioning.
    
*   If RViz isn’t displaying, check that topics are set up correctly and that ROS is sourced.
    

License

This project is under the MIT License. See the LICENSE file for details.

Acknowledgements

Special thanks to the communities behind OpenCV and ROS for their documentation:

*   OpenCV Documentation at docs.opencv.org
    
*   ROS Wiki at wiki.ros.org
    

Thank you for exploring this project. Enjoy learning about robotics and computer vision.