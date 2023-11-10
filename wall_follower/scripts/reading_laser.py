#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan

def callback_laser(msg):
    regions = [
        min(min(msg.ranges[0:143]),15),
        min(min(msg.ranges[144:287]),15),
        min(min(msg.ranges[288:431]),15),
        min(min(msg.ranges[432:575]),15),
        min(min(msg.ranges[576:713]),15)
    ]
    rospy.loginfo(regions)

def main():
    rospy.init_node('reading_laser')
    sub = rospy.Subscriber('/mp23/laser_scan',LaserScan, callback_laser)
    rospy.spin()

if __name__ == '__main__':
    main()

