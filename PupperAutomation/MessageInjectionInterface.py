from multiprocessing import connection
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
        huskystart()
    def injectionLoop(self):
        self.connection.send(msg_Trot(interrupt=False))
        while True:
            
            self.connection.send(msg_Forwards())
            print(self.lidar.recv())
            while self.lidar.recv() < 500:
                print(self.lidar.recv())
                self.connection.send(msg_Turn_Right())
                
            # huskySniff()
