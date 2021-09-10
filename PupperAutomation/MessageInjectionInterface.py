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
        
        # if __name__ == '__main__':
        # lidar_conn, lidar_injection_conn = Pipe()
        
        # lidar = LIDAR(lidar_injection_conn)
        # self.lidar_conn = lidar_conn
        # self.lidar = lidar
        
        self.connection.send(msg_Activation())
        # huskystart()
    def injectionLoop(self):
        
        while True:
            print("test")
            print(self.lidar.recv())

            if self.lidar.recv() < 200:
                self.connection.send(msg_Height_Decrease(80))
                self.connection.send(msg_Height_Increase(80))
                time.sleep(1.6)
            else:
                self.connection.send(msg_Trot(interrupt=False))
                time.sleep(1)
                