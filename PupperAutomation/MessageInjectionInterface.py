from multiprocessing import connection
from .behaviorFunctions import *
from .HuskyLens import *
from .LIDAR import *
from .BehaviourScripts import *

class MessageInjectionInterface:
    def __init__(self, ActionLoopConnection: connection.Connection):
        self.connection = ActionLoopConnection
        huskystart()
        lidarstart()

        self.connection.send(msg_Activation())
        
    def injectionLoop(self):

        while True:
            # wiggleForFriends(self)
            lidarscan()
            # frens = huskyCount()
            # print(frens)
            # lidartest()
            
        
        
