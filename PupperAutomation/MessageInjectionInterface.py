from multiprocessing import connection
from .behaviorFunctions import *
import time
from .openmvAprilTest import *
import random

class MessageInectionInterface:
    def __init__(self, ActionLoopConnection: connection.Connection):
        self.connection = ActionLoopConnection
        sensorOpen()

    def playDead(self):
        self.connection.send(msg_Height_Decrease(100))
        self.connection.send(msg_Wait(500))

    def injectionLoop(self):

        #self.connection.send(msg_Activation())
        
        #self.connection.send(msg_Trot(interrupt = True))
        #self.connection.send(msg_Turn_Left(500))
        #self.connection.send(msg_Wait(100))
        #self.connection.send(msg_Pitch_Up(50))
        #self.connection.send(msg_Strafe_Left(200))
       
       
        """state=1
        temp=0
        while 1 :
            temp=sensorGetTemp()
            print(temp)
            if temp >= 37:
                if state==1:
                    print("warm")
                    print("Slowly sit down")
                    print("wait 5s")
                    state=0
                    #time.sleep(5)
                else:
                    print("waiting...")
            else:
                if state == 0:
                    print("cold")
                    print("stand up")
                    print("wait 5s")
                    state=1
                    #time.sleep(5)
                else:
                    print("waiting...---")
            time.sleep(1)
            """
        #self.connection.send(msg_Trot(interrupt=False))
        state=1
        temp=0
        ran=1
        while 1 :
            temp=sensorGetTemp()
            print(temp)
            if temp >= 37:
                if state==1:
                    self.connection.send(msg_Height_Decrease(70))
                    time.sleep(0.7)
                    state=0
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
                    state=1
                ran=random.randint(1,7)
                #ran=1
                if(ran==1):
                    self.connection.send(msg_Trot(interrupt=False))
                    self.connection.send(msg_Pitch_Up(90))
                    self.connection.send(msg_Pitch_Down(90))
                    self.connection.send(msg_Trot(interrupt=False))
                    time.sleep(1.8)
                    
                elif(ran==2):
                    self.connection.send(msg_Trot(interrupt=False))
                    self.connection.send(msg_Turn_Left(300))
                    self.connection.send(msg_Trot(interrupt=False))
                    time.sleep(3)
                    
                elif(ran==3):
                    self.connection.send(msg_Trot(interrupt=False))
                    self.connection.send(msg_Strafe_Right(100))
                    self.connection.send(msg_Strafe_Left(100))
                    self.connection.send(msg_Trot(interrupt=False))
                    time.sleep(2)
                    
                elif(ran==4):
                    self.connection.send(msg_Trot(interrupt=False))
                    self.connection.send(msg_Backwards(120))
                    self.connection.send(msg_Trot(interrupt=False))
                    time.sleep(1.2)
                    
                elif(ran==5):
                    
                    self.connection.send(msg_Hop(30))
                    self.connection.send(msg_Hop(50))
                    time.sleep(0.8)
                    
                elif(ran==6):
                    self.connection.send(msg_Trot(interrupt=False))
                    self.connection.send(msg_Pitch_Up(100))
                    self.connection.send(msg_Yaw_Right(40))
                    self.connection.send(msg_Pitch_Down(100))
                    self.connection.send(msg_Trot(interrupt=False))
                    time.sleep(2.4)
                    
                elif(ran==7): 
                    self.connection.send(msg_Height_Decrease(80))
                    self.connection.send(msg_Pitch_Down(100))
                    self.connection.send(msg_Height_Increase(80))
                    time.sleep(2.6)
                    
            self.connection.send(msg_Wait(200))
            #time.sleep(1)
                    
                    
                    
            #self.connection.send(msg_Wait(100))
            #time.sleep(1)
            
        #self.connection.send(msg_Strafe_Right(100))
        
        #self.connection.send(msg_Generic)
        #self.connection.send(msg_Trot(interrupt = True))
        #self.connection.send(msg_Trot(interrupt = True))
        #self.connection.send(msg_Hop)
        
        #self.connection.send(msg_Pitch_Up(100))
        #self.connection.send(msg_Activation())
        
        #self.injection.send(msg_Pitch_Up(500))
        #self.connection.send(msg_Generic(ticks = 500, roll_left = 1))

        #self.connection.send(msg_Backwards(ticks=500))
        #self.connection.send(msg_Trot())"""
        """""
        while 1:
            temp=sensorGetTemp()
            print(temp)
            time.sleep(5)
        """""
            
        
        #print("injection sendt")
        sensorClose()

