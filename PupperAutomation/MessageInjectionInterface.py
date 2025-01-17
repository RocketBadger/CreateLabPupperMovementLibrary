from multiprocessing import connection
import multiprocessing
from .behaviorFunctions import *

class MessageInjectionInterface:
    def __init__(self, ActionLoopConnection: connection.Connection, lidar_conn: connection.Connection, husky_conn: connection.Connection):
        self.connection = ActionLoopConnection   
        # HUSKYLENS and in particular the LIDAR have both been given a multiprocessing pipe, to avoid the robot getting stuck waiting for input during its "while True" loop
        self.lidar = lidar_conn
        self.husky = husky_conn
        
        self.connection.send(msg_Activation())

    # This is the main "do stuff" loop
    # Here you can change what the robot actually *does* during its runtime
    def injectionLoop(self):
        conlist = [self.connection, self.lidar]
        
        self.connection.send(msg_Trot(interrupt=False))

        while True:
            multiprocessing.connection.wait(conlist)
            
            self.connection.send(msg_Forwards())

            while self.lidar.recv() <= 800:
                print(self.lidar.recv())
                self.connection.send(msg_Turn_Right())
            if self.husky.poll():
                print(self.husky.recv())
