#!/usr/bin/env python

import cv2 as cv
import rospy
import pytesseract
import numpy as np
import time
import yaml
from std_msgs.msg import String
import PyPDF2

# ADDING path
class Read():

    def __init__(self, address = None):
        self.address = address
        self.address_to_sparsh = rospy.get_param('address_to_sparsh')
        self.address_img = ""
        self.address_txt = ""
        self.address_pdf = ""
        self.file_extension = ""
        self.img_extensions = ["jpg", "png", "jpeg"]
        self.rate = rospy.get_param('current_rate')
        self.r = rospy.Rate(self.rate)
        self.string = ""
        self.state = rospy.get_param('current_mode')
        self.braille_dict = None
        self.pub = rospy.Publisher('two_digits', String, queue_size=100)


    def address_allocation(self):
        for pos, char in enumerate(self.address):
            if char == '.':
                self.file_extension = self.address[pos+1:]

        if self.file_extension in self.img_extensions:
            self.address_img = self.address

        elif self.file_extension == "txt":
            self.address_txt = self.address
        
        elif self.file_extension == "pdf":
            self.address_pdf = self.address
        
        else:
            print(" FILE EXTENSION {} is not supported.".format(self.file_extension))
    
    def image_manip(self):
        if len(self.address_img) != 0:
            self.kernel = np.ones((2,1), np.uint8)
            self.img = cv.imread(self.address_to_sparsh + self.address_img)
            erode = cv.erode(self.img, self.kernel, iterations=1)
            dilate = cv.dilate(erode, self.kernel, iterations=1)
            self.string = (pytesseract.image_to_string(dilate)).lower()

    def txt_manip(self):
        if len(self.address_txt) != 0:
            with open(self.address_to_sparsh + self.address_txt) as myfile:
                self.string="".join(line.rstrip() for line in myfile)
                print(self.string)

    def pdf_manip(self):
        if len(self.address_pdf) != 0:
            pdf = open(self.address_to_sparsh + self.address_pdf , 'rb')
            pdf_reader = PyPDF2.PdfFileReader(pdf)
            page_obj = pdf_reader.getPage(0)
            self.string = page_obj.extractText()
            self.string = self.string.replace('\n', ' ')
            print(self.string)
            

    def get_braille(self):
        with open(self.address_to_sparsh + '/src/sparsh_computation/config/braille_dict.yaml', 'r') as yaml_file:
            self.braille_dict = yaml.load(yaml_file, Loader=yaml.FullLoader) 

    def string_to_twodigits(self):
        while not rospy.is_shutdown():
            print ("Waiting")
            time.sleep(1)
            self.state = rospy.get_param('current_mode')
            if self.state == 'reading':
                break

        for i in range(len(self.string) - 1):
            try:
                x = String()
                x.data = str(self.braille_dict[self.string[i]]).zfill(2)
                self.pub.publish(x)
                self.rate = rospy.get_param('current_rate')
                self.r = rospy.Rate(self.rate)
                print(self.rate)
                self.r.sleep()


            except KeyError:
                pass
        
if __name__ == "__main__":
    rospy.init_node("reader")
    obj = Read("/he/tty.jpeg")
    obj.address_allocation()
    obj.image_manip()
    obj.txt_manip()
    obj.pdf_manip()
    