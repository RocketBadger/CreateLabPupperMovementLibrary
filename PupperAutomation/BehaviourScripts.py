from PupperAutomation.LIDAR import lidargo, lidartest
from .behaviorFunctions import *
import time
from .openmvAprilTest import *
import random
from .HuskyLens import *

        # REMEMBER TO RUN SUDO PIGPIOD, OR SUFFER INPUT/OUTPUT ERROR
        # This error can also occur if power to LIDAR module is insufficient!
        # 'incorrect starting description bytes' error appears to be a 50/50 chance right now, just run the program again
        # NOTE: maybe due to no stopping of LIDAR between runs?

def wiggleForFriends(self):
    frens = huskyCount()
    if frens > 0:
        print(huskyCount())
        self.connection.send(msg_Height_Decrease(80))
        self.connection.send(msg_Pitch_Down(100))
        self.connection.send(msg_Height_Increase(80))
        time.sleep(2.6)
    else:
        self.connection.send(msg_Trot(interrupt=False))
        self.connection.send(msg_Wait(90))
        self.connection.send(msg_Trot(interrupt=False))
        self.connection.send(msg_Yaw_Left(50))
        self.connection.send(msg_Trot(interrupt=False))
        self.connection.send(msg_Wait(90))
        self.connection.send(msg_Trot(interrupt=False))
        self.connection.send(msg_Yaw_Right(50))
        self.connection.send(msg_Wait(300))
        time.sleep(5.8)

def huskyLidarPrintTest():
    huskystart()
    lidargo()
    while True:
        frens = huskyCount()
        print(frens)
        lidartest()

def randomActionLoop(self):
    # remember to uncomment sensor code if using infrared temp!
    #self.connection.send(msg_Trot(interrupt=False))
    state = 1
    temp = 0
    ran = 1
    while 1:
            # temp=sensorGetTemp()
            # print(temp)
        if temp >= 37:
            if state == 1:
                self.connection.send(msg_Height_Decrease(70))
                time.sleep(0.7)
                state = 0
            self.connection.send(msg_Wait(500))
            self.connection.send(msg_Yaw_Left(30))
            self.connection.send(msg_Wait(90))
            self.connection.send(msg_Yaw_Right(30))
            self.connection.send(msg_Wait(30))
            time.sleep(6.8)
        else:
            if state == 0:
                self.connection.send(msg_Height_Increase(70))
                time.sleep(0.7)
                state = 1
            ran = random.randint(1, 7)
            if(ran == 1):
                self.connection.send(msg_Trot(interrupt=False))
                self.connection.send(msg_Pitch_Up(90))
                self.connection.send(msg_Pitch_Down(90))
                self.connection.send(msg_Trot(interrupt=False))
                time.sleep(1.8)
            elif(ran == 2):
                self.connection.send(msg_Trot(interrupt=False))
                self.connection.send(msg_Turn_Left(300))
                self.connection.send(msg_Trot(interrupt=False))
                time.sleep(3)
            elif(ran == 3):
                self.connection.send(msg_Trot(interrupt=False))
                self.connection.send(msg_Strafe_Right(100))
                self.connection.send(msg_Strafe_Left(100))
                self.connection.send(msg_Trot(interrupt=False))
                time.sleep(2)
            elif(ran == 4):
                self.connection.send(msg_Trot(interrupt=False))
                self.connection.send(msg_Backwards(120))
                self.connection.send(msg_Trot(interrupt=False))
                time.sleep(1.2)
            # elif(ran==5):

                # self.connection.send(msg_Hop(30))
                # self.connection.send(msg_Hop(50))
                # time.sleep(0.8)
            elif(ran == 6):
                self.connection.send(msg_Trot(interrupt=False))
                self.connection.send(msg_Pitch_Up(100))
                self.connection.send(msg_Yaw_Right(40))
                self.connection.send(msg_Pitch_Down(100))
                self.connection.send(msg_Trot(interrupt=False))
                time.sleep(2.4)
            elif(ran == 7):
                self.connection.send(msg_Height_Decrease(80))
                self.connection.send(msg_Pitch_Down(100))
                self.connection.send(msg_Height_Increase(80))
                time.sleep(2.6)
        self.connection.send(msg_Wait(200))
    # sensorClose()

def playDead(self):
    self.connection.send(msg_Height_Decrease(100))
    self.connection.send(msg_Wait(500))
