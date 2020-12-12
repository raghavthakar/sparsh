#!/usr/bin/python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sparsh_gui_1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyttsx3
import yaml

#SETTING UP TEXT TO SPEECH FOR NOTIFYING
engine = pyttsx3.init()
engine.setProperty('rate', 125)

class Ui_Form(object):

    def __init__(self):
        self.current_mode="default" #STORES CURRENT STATE IN A STRING
        # MODES ARE:
        # default
        # recording
        # memory
        # reading
        # recalling

        #DATA TO BE WRITTEN ONTO YAML FILE
        self.yaml_data = {'current_mode' : self.current_mode}, {'rate' : 0.5}
        with open('data/sparsh_state.yaml', 'w') as yaml_file:
            documents = yaml.dump(self.yaml_data, yaml_file)

    #INITIALISE THE UI ELEMENTS
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 350)

        #SETTING UP THE BASICS FOR EVERY INPUT
        self.speed_dial = QtWidgets.QDial(Form)
        self.speed_dial.setGeometry(QtCore.QRect(225, 50, 100, 100))
        self.speed_dial.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.speed_dial.setProperty("value", 50)
        self.speed_dial.setObjectName("speed_dial")
        self.scroll_dial = QtWidgets.QDial(Form)
        self.scroll_dial.setGeometry(QtCore.QRect(75, 50, 100, 100))
        self.scroll_dial.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.scroll_dial.setMinimum(0)
        self.scroll_dial.setMaximum(9)
        self.scroll_dial.setSingleStep(1)
        self.scroll_dial.setProperty("value", 5)
        self.scroll_dial.setSliderPosition(0)
        self.scroll_dial.setObjectName("scroll_dial")
        self.scroll_label = QtWidgets.QLabel(Form)
        self.scroll_label.setGeometry(QtCore.QRect(100, 30, 50, 20))
        self.scroll_label.setAlignment(QtCore.Qt.AlignCenter)
        self.scroll_label.setObjectName("scroll_label")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(250, 30, 50, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.memory_button = QtWidgets.QPushButton(Form)
        self.memory_button.setGeometry(QtCore.QRect(75, 175, 100, 50))
        self.memory_button.setObjectName("memory_button")
        self.start_stop_button = QtWidgets.QPushButton(Form)
        self.start_stop_button.setGeometry(QtCore.QRect(225, 175, 100, 50))
        self.start_stop_button.setObjectName("start_stop_button")
        self.record_button = QtWidgets.QPushButton(Form)
        self.record_button.setGeometry(QtCore.QRect(150, 250, 100, 50))
        self.record_button.setObjectName("record_button")

        #CONNECTING EACH INPUT TO THE CALLBACK
        #CALLBACK WHEN DIAL POSITION IS CHANGED
        self.speed_dial.valueChanged.connect(self.speedDialMoved)
        self.scroll_dial.valueChanged.connect(self.scrollDialMoved)

        #CALLBACK FOR THE BUTTONS
        self.start_stop_button.clicked.connect(self.startStopClicked)
        self.record_button.clicked.connect(self.recordClicked)
        self.memory_button.clicked.connect(self.memoryClicked)

        #SET UP THE RIGHT NAME AND STUFF
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def rangeMap(self, dial_val):
        if dial_val>0:
            return ((dial_val)*(2-0.25)/(100)+0.25)
        else:
            return 0.25

    #CALLBACK DEFINITIONS
    def speedDialMoved(self):
        #UPDATE STATE IN FILE
        #MAP FROM 0.25 TO 2 (ONE EVERY 4 SECS TO 2 TIMES EVERY SEC)
        self.yaml_data = {'current_mode' : self.current_mode}, {'rate' : self.rangeMap(self.speed_dial.value())}
        with open('data/sparsh_state.yaml', 'w') as yaml_file:
            documents = yaml.dump(self.yaml_data, yaml_file)

    def scrollDialMoved(self):
        print("Scroll dial value = %i" % (self.scroll_dial.value()))

    #HANDLES START STOP BUTTON CLICK
    def startStopClicked(self):
        if self.current_mode is "reading":
            self.current_mode="default"
        elif self.current_mode is "default":
            self.current_mode="reading"
        elif self.current_mode is "memory":
            self.current_mode="recalling"
            self.notify("Recalling text corresponding to %i" % (self.scroll_dial.value()))
        elif self.current_mode is "recalling":
            self.current_mode="memory"
        else:
            self.notify("You're in "+ self.current_mode +". Please stop recording first.")
        self.notify("Current mode is "+self.current_mode)
        #UPDATE STATE IN FILE
        self.yaml_data = {'current_mode' : self.current_mode}, {'rate' : self.rangeMap(self.speed_dial.value())}
        with open('data/sparsh_state.yaml', 'w') as yaml_file:
            documents = yaml.dump(self.yaml_data, yaml_file)

    # HANDLES RECORD BUTTON CLICK
    def recordClicked(self):
        if self.current_mode is "recording":
            self.current_mode = "default"
        elif self.current_mode is "default":
            self.current_mode = "recording"
        else:
            self.notify("Cannot record. Please exit to default state.")
        self.notify("Current mode is "+self.current_mode)
        #UPDATE STATE IN FILE
        self.yaml_data = {'current_mode' : self.current_mode}, {'rate' : self.rangeMap(self.speed_dial.value())}
        with open('data/sparsh_state.yaml', 'w') as yaml_file:
            documents = yaml.dump(self.yaml_data, yaml_file)

    # HANDLES MEMORY BUTTON CLICK
    def memoryClicked(self):
        if self.current_mode is "default":
            self.current_mode="memory"
        elif self.current_mode is "memory":
            self.current_mode="default"
        else:
            self.notify("You're in "+ self.current_mode +". Please exit to default state.")
        self.notify("Current mode is "+self.current_mode)
        #UPDATE STATE IN FILE
        self.yaml_data = {'current_mode' : self.current_mode}, {'rate' : self.rangeMap(self.speed_dial.value())}
        with open('data/sparsh_state.yaml', 'w') as yaml_file:
            documents = yaml.dump(self.yaml_data, yaml_file)

    #HANDLE ANY NOTIFICATION
    def notify(self, notify_message):
        print(notify_message)
        engine.say(notify_message)
        engine.runAndWait()

    #FINISHING TOUCHED TO THE UI
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sparsh GUI"))
        Form.setWindowIcon(QtGui.QIcon('assets/asset5.png'))
        self.scroll_label.setText(_translate("Form", "Scroll"))
        self.label.setText(_translate("Form", "Speed"))
        self.memory_button.setText(_translate("Form", "Memory"))
        self.start_stop_button.setText(_translate("Form", "Start/Stop"))
        self.record_button.setText(_translate("Form", "Record"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
