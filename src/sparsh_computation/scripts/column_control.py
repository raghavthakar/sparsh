#!/usr/bin/env python

# Importing the required libraries
import rospy
from std_msgs.msg import Float64, String
import time
import math
import numpy as np

class Controller():

    def __init__(self):
        # initializing ros node with name node_sparsh_controller
        rospy.init_node('node_sparsh_controller')

        # sample rate
        self.sample_rate = 60  # in Hz
        self.string =""
        self.sleep_rate = 1.5
        self.num = None
        self.num_left = ""
        self.num_right = ""
        # publishers
        self.top_right = rospy.Publisher('/sparsh/top_right_column_to_base_link_position_controller/command', Float64, queue_size=10)
        self.top_left = rospy.Publisher('/sparsh/top_left_column_to_base_link_position_controller/command', Float64, queue_size=10)
        self.middle_right = rospy.Publisher('/sparsh/middle_right_column_to_base_link_position_controller/command', Float64, queue_size=10)
        self.middle_left = rospy.Publisher('/sparsh/middle_left_column_to_base_link_position_controller/command', Float64, queue_size=10)
        self.bottom_right = rospy.Publisher('/sparsh/bottom_right_column_to_base_link_position_controller/command', Float64, queue_size=10)
        self.bottom_left = rospy.Publisher('/sparsh/bottom_left_column_to_base_link_position_controller/command', Float64, queue_size=10)

        self.func_dict = {
        "00": self.reset_left,
        "10": self._10, 
        "20": self._20 , 
        "30": self._30, 
        "40": self._40,
        "50": self._50,
        "60": self._60,
        "70": self._70,
        "0": self.reset_right,
        "1": self._1, 
        "2": self._2 , 
        "3": self._3, 
        "4": self._4,
        "5": self._5,
        "6": self._6,
        "7": self._7
        }
        rospy.Subscriber('/two_digits', String , callback=self.ocr_callback)

    # Callbacks
    def ocr_callback(self, msg):
        self.num = int(msg.data)
        self.num_left, self.num_right = self.number_filter(num=self.num)
    
    
    def number_filter(self, num):
        num_right = math.fmod(num, 10) 
        num_left = num // 10

        print(str(num_left*10) + "   ---   " + str(num_right))
        
        num_left *= 10
        num_right = str(int(num_right))
        
        if num_left == 0:
            num_left = str(num_left).zfill(2)
        else:
            num_left = str(num_left)
        return num_left, num_right

    def all_up(self):
        self.top_right.publish(1.0)
        self.top_left.publish(1.0)
        self.middle_right.publish(1.0)
        self.middle_left.publish(1.0)
        self.bottom_right.publish(1.0)
        self.bottom_left.publish(1.0)

    def reset(self):
        self.top_right.publish(.0)
        self.top_left.publish(.0)
        self.middle_right.publish(.0)
        self.middle_left.publish(.0)
        self.bottom_right.publish(.0)
        self.bottom_left.publish(.0)
    
    def reset_left(self):
        self.top_left.publish(.0)
        self.middle_left.publish(.0)
        self.bottom_left.publish(.0)

    def reset_right(self):
        self.top_right.publish(.0)
        self.middle_right.publish(.0)
        self.bottom_right.publish(.0)

    def _10(self):
        self.reset_left()
        self.bottom_left.publish(1.)
    
    def _20(self):
        self.reset_left()
        self.middle_left.publish(1.)

    def _30(self):
        self.reset_left()
        self.bottom_left.publish(1.)
        self.middle_left.publish(1.)
    
    def _40(self):
        self.reset_left()
        self.top_left.publish(1.)

    def _50(self):
        self.reset_left()
        self.top_left.publish(1.)
        self.bottom_left.publish(1.)

    def _60(self):
        self.reset_left()
        self.top_left.publish(1.)
        self.middle_left.publish(1.)

    def _70(self):
        self.reset_left()
        self.middle_left.publish(1.)
        self.top_left.publish(1.)
        self.bottom_left.publish(1.)
    
    def _1(self):
        self.reset_right()
        self.bottom_right.publish(1.)

    def _2(self):
        self.reset_right()
        self.middle_right.publish(1.)

    def _3(self):
        self.reset_right()
        self.bottom_right.publish(1.)
        self.middle_right.publish(1.)

    def _4(self):
        self.reset_right()
        self.top_right.publish(1.)

    def _5(self):
        self.reset_right()
        self.bottom_right.publish(1.)
        self.top_right.publish(1.)

    def _6(self):
        self.reset_right()
        self.middle_right.publish(1.)
        self.top_right.publish(1.)

    def _7(self):
        self.reset_right()
        self.bottom_right.publish(1.)
        self.middle_right.publish(1.)
        self.top_right.publish(1.)

    def Control(self):
        try:
            time.sleep(.5)
            self.func_dict[self.num_left]()
            self.func_dict[self.num_right]()
            time.sleep(.5)
        except:
            pass



if __name__ == '__main__':
    box = Controller()
    r = rospy.Rate(box.sample_rate)
    while not rospy.is_shutdown():
        box.Control()
        r.sleep()
