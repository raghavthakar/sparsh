#!/usr/bin/env python

import cv2 as cv
import rospy
import pytesseract
import numpy as np
import time 

class Text_Manipulation:

    def __init__(self, address = "/home/pkvk/word-random-text.png"):
        self.kernel = np.ones((2,1), np.uint8)
        self.img = cv.imread(address)
        self.sleeptime = rospy.get_param('current_rate')
        self.string = None
        self.state = rospy.get_param('current_node')
        self.braille = rospy.get_param('braille')                     


    def manip(self):

        erode = cv.erode(self.img, self.kernel, iterations=1)
        dilate = cv.dilate(erode, self.kernel, iterations=1)

        self.string = (pytesseract.image_to_string(dilate)).lower()

    def string_to_twodigits(self):

        if self.state == 'reading':
            for i in range(len(self.string) - 1):
                rospy.set_param('two_digits', int(str(self.braille[self.string[i]]) + str(self.braille[self.string[i+1]])))
                time.sleep(int(self.sleeptime))

if __name__ == '__main__':
    rospy.init_node('ocr')
    t = Text_Manipulation()
    t.manip()
    t.string_to_twodigits()

