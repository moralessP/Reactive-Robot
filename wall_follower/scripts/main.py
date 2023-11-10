#! /usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class WallFollower:
    def __init__(self):
        rospy.init_node('wall_follower')
        rospy.Subscriber('/mp23/laser_scan', LaserScan, self.laser_callback)
        rospy.Subscriber('/mp23/odom', Odometry, self.finish)
        self.cmd_vel_pub = rospy.Publisher('/mp23/cmd_vel', Twist, queue_size=1)
        self.twist = Twist()
        self.goal_pos = False

    def laser_callback(self, data):
        """
            This function reads values from the Lidar and send cmd to /mp23/cmd_vel topic 
        """
        ranges = data.ranges

        min_distance = min(ranges[0:575])

        if not self.goal_pos:
            if min_distance < 0.8: 
                rospy.loginfo("Turn Left and follow")
                self.twist.linear.x = 0.5
                self.twist.angular.z = -0.3 
            else:
                rospy.loginfo("Turn right and follow")
                self.twist.linear.x = 0.4 
                self.twist.angular.z = 0.3
            self.cmd_vel_pub.publish(self.twist)
        else:
            rospy.loginfo("Finish")
            self.twist.linear.x = 0.0
            self.twist.angular.z = 0.0
            self.cmd_vel_pub.publish(self.twist)
    
    def finish(self, odom_msg):
        """
            This function reads values from odom and set if the robot is at the goal position
        """
        position = odom_msg.pose.pose.position
        if -0.3 < position.y and position.y < 0.3 and position.x <-7:
            self.goal_pos = True 

if __name__ == '__main__':
    wall_follower = WallFollower()
    rospy.spin()