#!/usr/bin/env python

import yaml
import time
import rospy


current_mode="bruh"
current_rate=23

address_to_sparsh = rospy.get_param('address_to_sparsh')

with open(address_to_sparsh + '/src/gui/scripts/data/sparsh_state.yaml', 'r') as yaml_file:
    yaml_data = yaml.load(yaml_file, Loader=yaml.FullLoader)
    rospy.set_param('current_rate',(yaml_data[3]['default_rate']))
    rospy.set_param('current_mode',(yaml_data[2]['default_mode']))
    print(rospy.get_param('current_rate'))



while True:
    previous_mode=rospy.get_param('current_mode')
    previous_rate=rospy.get_param('current_rate')
    with open(address_to_sparsh + '/src/gui/scripts/data/sparsh_state.yaml', 'r') as yaml_file:
        time.sleep(0.1)
        yaml_data = yaml.load(yaml_file, Loader=yaml.FullLoader)
        try:
            rospy.set_param('current_rate',(yaml_data[1]['rate']))
            rospy.set_param('current_mode',(yaml_data[0]['current_mode']))
        except:
            pass

    if rospy.get_param('current_rate') != previous_rate:
        print(rospy.get_param('current_rate'))

    if rospy.get_param('current_mode') != previous_mode:
        print(rospy.get_param('current_mode'))
