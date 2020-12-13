#!/usr/bin/env python

import cv2 as cv
import rospy
import pytesseract
import numpy as np
import time
import yaml
from std_msgs.msg import String

class Memory:

    def __init__(self):
        self.reset_memory()
        self.pub = rospy.Publisher('recall', String, queue_size=100)
        self.sub = rospy.Subscriber('record', String, self.record_into_memory)

    def reset_memory(self):
        rospy.set_param('0','')
        rospy.set_param('1','')
        rospy.set_param('2','')
        rospy.set_param('3','')
        rospy.set_param('4','')
        rospy.set_param('5','')
        rospy.set_param('6','')
        rospy.set_param('7','')
        rospy.set_param('8','')
        rospy.set_param('9','')

    def record_into_memory(self,content):
        while rospy.get_param('current_mode') == 'recording':
            rospy.set_param(str(rospy.get_param('current_scroll_position')), str(content))

    def recall(self):
        while rospy.get_param('current_mode') == 'recalling':
            x = String()
            key = rospy.get_param('current_scroll_position')
            x.data = rospy.get_param(str(key))
            self.pub.publish(x)

    def string_to_twodigits(self):
        while not rospy.is_shutdown():
            """
            Under Construction
           """ 
            pass
