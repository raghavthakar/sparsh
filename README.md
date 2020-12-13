![picture](readme_assets/Asset_1.png)
# Sparsh


## HackOff 3.0 project. A braille reader for everything!

### Team Name: Team Suroor
### Track: Robotics, Beginners
### Members: Keshav Kapur, Kvk Praneeth, and Raghav Thakar
### The future is accessible, and this is how we get there.

Welcome to our repository. Sparsh is a device that we made so that we 
can help blind people read anytime and anywhere. The average device that blind people use cost above 1 lakh rupees but we've found a low cost efficient solution "Sparsh".


Sparsh has a camera at it's bottom which will read any document kept under it. Once the document text is read, the user could keep his/her hand on the 6 cylinder actuators to feel the output. To make the reading more comprehensive we have added a speaker to the node and a headphone jack to the device so the user can listen to what they're reading while feeling the braille output.

![picture](readme_assets/sparsh_v13_camera.PNG)
![picture](readme_assets/sparsh_v13_closeup.PNG)
![picture](readme_assets/sparsh_v13_front_top.PNG)
![picture](readme_assets/gif_1.gif)

Dependecy list to run the simulation and the gui:

* Python 2 
* Python 3
* ROS barebones
* PyQt5 (pip3)
* pyttsx3 (pip3)
* pyttsx (pip2)
* espeak (sudo apt install espeak)
* Gazebo
* pyyaml(pip3)
* pyyaml(pip2)
* datetime(pip3)
* PyPDF2(pip)
* Opencv-python(pip)
* Numpy(pip)
* pytesseract(pip)

Setting up the directory:



```
cd ~/sparsh/src/gui/scripts
```
Open the text file and replace your laptop's id inside the setup.sh
![picture](readme_assets/setup.png)

```
source setup.sh
```

To run the gui:
```
cd ~/sparsh/src/gui/scripts/ && python3 sparsh_gui_1.py
```

To run the simulation on Gazebo:
```
cd ~/sparsh

catkin_make

source devel/setup.bash

roslaunch sparsh_computation sparsh.launch
```


