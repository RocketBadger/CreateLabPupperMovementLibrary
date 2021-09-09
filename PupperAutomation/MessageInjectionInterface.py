from multiprocessing import connection
from .behaviorFunctions import *
import time
from .openmvAprilTest import *
import random
from .HuskyLens import *
from .LIDAR import *
from .BehaviourScripts import *

class MessageInjectionInterface:
    def __init__(self, ActionLoopConnection: connection.Connection):
        self.connection = ActionLoopConnection
        huskystart()
        lidargo()

        self.connection.send(msg_Activation())

        # REMEMBER TO RUN SUDO PIGPIOD, OR SUFFER INPUT/OUTPUT ERROR
        # This error can also occur if power to LIDAR module is insufficient!
        # 'incorrect starting description bytes' error appears to be a 50/50 chance right now, just run the program again
        
    def injectionLoop(self):

        while True:
            wiggleForFriends(self)
            # frens = huskyCount()
            # print(frens)
            # lidartest()
            
        
        
