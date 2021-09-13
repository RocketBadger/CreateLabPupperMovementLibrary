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
        self.connection.send(msg_Trot(interrupt=False))
        # time.sleep(1)
        while True:
            # print("test")
            self.connection.send(msg_Forwards())
            print(self.lidar.recv())
            while self.lidar.recv() < 600:
                # self.connection.send(msg_Trot(interrupt=False))
                # self.connection.send(msg_Height_Decrease(80))
                # self.connection.send(msg_Height_Increase(80))
                # self.connection.send(msg_Trot(interrupt=False))
                self.connection.send(msg_Turn_Right())
                # time.sleep(2.5)
            # time.sleep(0.1)
                
                