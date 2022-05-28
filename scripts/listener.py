#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Empty

time_robot_start = rospy.Duration(0)

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    now = rospy.get_rostime()
    rospy.loginfo("Current time %i %i %f", now.secs, now.nsecs, rospy.get_time())
    

def callback_robot_start(data):
    global time_robot_start
    time_robot_start = rospy.get_time()

def callback_robot_finish(data):
    global time_robot_start
    time_robot_finish = rospy.get_time()
    rospy.loginfo("Duration %f", time_robot_finish - time_robot_start)
    
def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", String, callback)
    
    rospy.Subscriber("robot_start", String, callback_robot_start)
    rospy.Subscriber("robot_finish", String, callback_robot_finish)


    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()