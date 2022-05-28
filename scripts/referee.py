#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Empty

time_robot_start = rospy.Duration(0)

def callback_robot_start(data):
    global time_robot_start
    time_robot_start = rospy.get_time()
    rospy.loginfo("Robot start time %f", time_robot_start)

def callback_robot_finish(data):
    global time_robot_start
    time_robot_finish = rospy.get_time()
    rospy.loginfo("Time for the robot to complete the competition Name_team=%s Ros_now=%f Duration=%f", data.data , time_robot_finish, time_robot_finish - time_robot_start)
    
def listener():
    rospy.init_node('listener', anonymous=True)
    
    rospy.Subscriber("robot_start", Empty, callback_robot_start)
    rospy.Subscriber("robot_finish", String, callback_robot_finish)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()