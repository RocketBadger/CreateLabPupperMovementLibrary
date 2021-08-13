from .behaviorFunctions import *
from queue import Queue
#from openmvAprilTest import *


def pivotTest():
    """
        returns a queue that only activates and then deactivates the robot.
    """
    actionsMessageQueue = Queue()

    actionsMessageQueue.put(msg_Activation())
    actionsMessageQueue.put(msg_Wait(50))
    actionsMessageQueue.put(msg_Trot())
    actionsMessageQueue.put(msg_Wait(50))
    actionsMessageQueue.put(msg_Turn_Left(150))
    actionsMessageQueue.put(msg_Wait(50))
    actionsMessageQueue.put(msg_Turn_Right(150))
    actionsMessageQueue.put(msg_Wait(50))
    actionsMessageQueue.put(msg_Trot())

    return actionsMessageQueue

def turningTest():
    """
        returns a queue that only activates and then deactivates the robot.
    """
    actionsMessageQueue = Queue()

    actionsMessageQueue.put(msg_Activation())
    actionsMessageQueue.put(msg_Wait(20))
    actionsMessageQueue.put(msg_Trot())
    actionsMessageQueue.put(msg_Wait(20))
    actionsMessageQueue.put(msg_Turn_Right(50))
    actionsMessageQueue.put(msg_Wait(20))
    actionsMessageQueue.put(msg_Forwards(100))
    actionsMessageQueue.put(msg_Wait(20))
    actionsMessageQueue.put(msg_Turn_Left(50))


    return actionsMessageQueue


def walkTest2():
    
    actionsMessageQueue = Queue()

    actionsMessageQueue.put(msg_Activation())
    actionsMessageQueue.put(msg_Trot())
    actionsMessageQueue.put(msg_Wait(1000))
    actionsMessageQueue.put(msg_Forwards(200))
    actionsMessageQueue.put(msg_Wait(100))
    actionsMessageQueue.put(msg_Strafe_Right(200))
    actionsMessageQueue.put(msg_Wait(100))
    actionsMessageQueue.put(msg_Strafe_Left(200))
    actionsMessageQueue.put(msg_Wait(100))
    actionsMessageQueue.put(msg_Backwards(200))
    actionsMessageQueue.put(msg_Wait(200))
    
    return actionsMessageQueue


def walkTest():
    
    actionsMessageQueue = Queue()

    actionsMessageQueue.put(msg_Activation())
    actionsMessageQueue.put(msg_Trot())
    actionsMessageQueue.put(msg_Wait(200))
    actionsMessageQueue.put(msg_Forwards(200))
    actionsMessageQueue.put(msg_Wait(100))
    actionsMessageQueue.put(msg_Strafe_Right(200))
    actionsMessageQueue.put(msg_Wait(100))
    actionsMessageQueue.put(msg_Strafe_Left(200))
    actionsMessageQueue.put(msg_Wait(100))
    actionsMessageQueue.put(msg_Backwards(200))
    actionsMessageQueue.put(msg_Wait(200))
    

    return actionsMessageQueue

def test():
    """
        returns a queue that only activates and then deactivates the robot.
    """
    actionsMessageQueue = Queue()

    actionsMessageQueue.put(msg_Activation())
    actionsMessageQueue.put(msg_Wait(200))
    actionsMessageQueue.put(msg_Trot())
    actionsMessageQueue.put(msg_Wait(200))
    actionsMessageQueue.put(msg_Yaw_Left(300))
    actionsMessageQueue.put(msg_Yaw_Right(600))
    actionsMessageQueue.put(msg_Yaw_Left(300))
    actionsMessageQueue.put(msg_Wait(200))
    actionsMessageQueue.put(msg_Trot())


    return actionsMessageQueue
    
def emptyQueue():
    actionsMessageQueue = Queue()
    actionsMessageQueue.put(msg_Activation())
  
    return actionsMessageQueue


def behavioerDemo():
    """
        returns a queue stacked with messages demoing activation, height, pitch, roll, and yaw messages.
    """

    actionsMessageQueue = Queue()

    actionsMessageQueue.put(msg_Activation())
    actionsMessageQueue.put(msg_Wait(100))

    actionsMessageQueue.put(msg_Height_Increase(90))
    actionsMessageQueue.put(msg_Wait(20))

    actionsMessageQueue.put(msg_Height_Decrease(90))
    actionsMessageQueue.put(msg_Wait(20))

    actionsMessageQueue.put(msg_Roll_Right(30))
    actionsMessageQueue.put(msg_Wait(20))

    actionsMessageQueue.put(msg_Roll_Left(30))
    actionsMessageQueue.put(msg_Wait(20))

    actionsMessageQueue.put(msg_Roll_Left(30))
    actionsMessageQueue.put(msg_Wait(20))

    actionsMessageQueue.put(msg_Roll_Right(30))
    actionsMessageQueue.put(msg_Wait(20))

    actionsMessageQueue.put(msg_Yaw_Left(20))
    actionsMessageQueue.put(msg_Wait(30))

    actionsMessageQueue.put(msg_Yaw_Right(40))
    actionsMessageQueue.put(msg_Wait(20))

    actionsMessageQueue.put(msg_Yaw_Left(20))
    actionsMessageQueue.put(msg_Wait(30))

    actionsMessageQueue.put(msg_Pitch_Up(20))
    actionsMessageQueue.put(msg_Wait(20))

    actionsMessageQueue.put(msg_Pitch_Down(40))
    actionsMessageQueue.put(msg_Wait(20))

    actionsMessageQueue.put(msg_Pitch_Up(20))
    actionsMessageQueue.put(msg_Wait(20))
    
    actionsMessageQueue.put(msg_Strafe_Left(120))
    actionsMessageQueue.put(msg_Wait(20))
    

    return actionsMessageQueue



def letsgooo():
    actionsMessageQueue = Queue()
    
    state=1
    temp=0
    while 1 :
        temp=sensorGetTemp()
        print(temp)
        if temp >= 37:
            if state==1:
                actionsMessageQueue.put(msg_Height_Decrease(100))
                actionsMessageQueue.put(msg_Wait(500))
                state=0
        else:
            if state == 0:
                actionsMessageQueue.put(msg_Height_Increase(100))
                state=1
                actionsMessageQueue.put(msg_Trot(interrupt=False))
                actionsMessageQueue.put(msg_Turn_Left(300))
                actionsMessageQueue.put(msg_Trot(interrupt=False))
        actionsMessageQueue.put(msg_Wait(100))