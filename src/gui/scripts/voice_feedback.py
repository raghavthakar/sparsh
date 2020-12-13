#!/usr/bin/env python

import yaml
import time
import rospy
import pyttsx

#SETTING UP TEXT TO SPEECH FOR NOTIFYING
engine = pyttsx.init()
engine.setProperty('rate', rospy.get_param('current_rate')*100)
current_mode=rospy.get_param('current_mode')

address_to_sparsh = rospy.get_param('address_to_sparsh')
string_file = open(address_to_sparsh + "/src/gui/scripts/data/string_for_voice.txt","r")
string_base=string_file.read()
string_file.close()

if current_mode=='reading' or 'recalling':
    engine.say(string_base)
    engine.runAndWait()

while not rospy.is_shutdown():
    current_mode=rospy.get_param('current_mode')
    string_file = open(address_to_sparsh + "/src/gui/scripts/data/string_for_voice.txt","r")
    string=string_file.read()
    string_file.close()
    if string!=string_base:
        string_base=string
        if current_mode=='reading' or 'recalling':
            engine.say(string)
            engine.runAndWait()
