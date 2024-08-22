#!/usr/bin/env python3
import rospy
if __name__ =='__main__' :
    rospy.init_node("test_node")

    rospy.loginfo(" test node is starting")

    rate=rospy.Rate(10)
while not rospy.is_shutdown():
    rospy.loginfo(" Hellow ")
    rate.sleep()    