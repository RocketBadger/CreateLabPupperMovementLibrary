from multiprocessing import connection
import multiprocessing
from .behaviorFunctions import *
from .HuskyLens import *
# from LIDAR import *
# import LIDAR
from .BehaviourScripts import *

class MessageInjectionInterface:
    def __init__(self, ActionLoopConnection: connection.Connection, lidar_conn: connection.Connection):
        self.connection = ActionLoopConnection   
        self.lidar = lidar_conn
        
        self.connection.send(msg_Activation())
        # huskystart()
        
    def injectionLoop(self):
        conlist = [self.connection, self.lidar]
        
        self.connection.send(msg_Trot(interrupt=False))
        while True:
            self.connection.send(msg_Forwards())
            multiprocessing.connection.wait(conlist)
            print(self.lidar.recv())
            while self.lidar.recv() < 500:
                # print(self.lidar.recv())
                self.connection.send(msg_Turn_Right())
                
            # huskySniff()
