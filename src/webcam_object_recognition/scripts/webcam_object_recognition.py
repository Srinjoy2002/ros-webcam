#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String  
from cv_bridge import CvBridge
import cv2

def webcam_object_recognition():
    rospy.init_node('webcam_object_recognition', anonymous=True)
    
    
    image_pub = rospy.Publisher('/webcam/image_with_detections', Image, queue_size=10)
    
    
    detected_object_pub = rospy.Publisher('detected_object', String, queue_size=10)

    bridge = CvBridge()
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

     
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        rospy.logerr("Cannot open webcam")
        return

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if not ret:
            rospy.logerr("Failed to capture image")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            
            detected_object_pub.publish("Object Detected: Face")  # Example label

        img_msg = bridge.cv2_to_imgmsg(frame, "bgr8")
        image_pub.publish(img_msg)

        cv2.imshow("Webcam Object Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        webcam_object_recognition()
    except rospy.ROSInterruptException:
        pass

