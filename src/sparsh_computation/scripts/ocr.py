#!/usr/bin/env python

import cv2 as cv
import rospy
import pytesseract
import numpy as np
import time 
import yaml
from std_msgs.msg import String

class Text_Manipulation:

    def __init__(self, address = "/home/pkvk/word-random-text.png"):
        self.kernel = np.ones((2,1), np.uint8)
        self.img = cv.imread(address)
        self.rate = rospy.get_param('current_rate')
        self.r = rospy.Rate(self.rate)
        self.string = None
        self.state = rospy.get_param('current_mode')
        self.braille_dict = None
        self.pub = rospy.Publisher('two_digits', String, queue_size=100)

    def get_braille(self):

        with open('/home/pkvk/sparsh/src/sparsh_computation/config/braille_dict.yaml', 'r') as yaml_file:
            self.braille_dict = yaml.load(yaml_file, Loader=yaml.FullLoader)

        

    def manip(self):

        erode = cv.erode(self.img, self.kernel, iterations=1)
        dilate = cv.dilate(erode, self.kernel, iterations=1)

        self.string = (pytesseract.image_to_string(dilate)).lower()

    def string_to_twodigits(self):

        if self.state == 'reading':
            for i in range(len(self.string) - 1):
                try:
                    x = String()
                    x.data = str(self.braille_dict[self.string[i]]).zfill(2)
                    self.pub.publish(x)
                    self.r.sleep()

                except:
                    pass

if __name__ == '__main__':
    rospy.init_node('ocr')
    t = Text_Manipulation()
    t.get_braille()
    t.manip()
    t.string_to_twodigits()
