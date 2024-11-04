#!/usr/bin/env python3

import rospy
from visualization_msgs.msg import Marker
from std_msgs.msg import String  

def create_marker(id, x, y, z, text):
    marker = Marker()
    marker.header.frame_id = "map"
    marker.header.stamp = rospy.Time.now()
    marker.ns = "webcam_object_recognition"
    marker.id = id
    marker.type = Marker.TEXT_VIEW_FACING
    marker.action = Marker.ADD
    marker.pose.position.x = x
    marker.pose.position.y = y
    marker.pose.position.z = z
    marker.text = text
    marker.scale.z = 0.5  
    marker.color.r = 1.0
    marker.color.g = 0.0
    marker.color.b = 0.0
    marker.color.a = 1.0
    return marker

def object_callback(msg):
    
    x, y, z = 1.0, 0.5, 1.0

    
    marker = create_marker(id=0, x=x, y=y, z=z, text=msg.data)
    marker_pub.publish(marker)

if __name__ == '__main__':
    rospy.init_node('visualization_node', anonymous=True)
    marker_pub = rospy.Publisher('visualization_marker', Marker, queue_size=10)
    rospy.Subscriber('detected_object', String, object_callback)  

    rospy.loginfo("RViz visualization node started.")
    rospy.spin()

