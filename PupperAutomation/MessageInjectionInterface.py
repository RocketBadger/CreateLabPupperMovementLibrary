from multiprocessing import connection
from .behaviorFunctions import *
from .HuskyLens import *
from .LIDAR import LIDAR
from .BehaviourScripts import *

class MessageInjectionInterface:
    def __init__(self, ActionLoopConnection: connection.Connection):
        self.connection = ActionLoopConnection   
        
        # if __name__ == '__main__':
        lidar_conn, lidar_injection_conn = Pipe()
        
        lidar = LIDAR(lidar_injection_conn)
        
        lidar_pipe = Process(target=lidar.lidarscan, args=())
        lidar_pipe.start()
        print("lidar pipe started")
        print(lidar_conn.recv())
        lidar_pipe.join()
        print("lidar pipe joined")
        
        self.connection.send(msg_Activation())

                
        
        # huskystart()
        LIDAR.lidarstart()

    def injectionLoop(self):
        # wiggleTooClose(self)
        # lScan = lidarscan()
        while True:
            print(self.lidar_conn.recv())
            # lScan = lidarscan()
            # wiggleForFriends(self)
            # while lScan < 200:
            #     self.connection.send(msg_Height_Decrease(80))
            #     self.connection.send(msg_Height_Increase(80))
            #     time.sleep(1.6)
            # else:
            #     self.connection.send(msg_Trot(interrupt=False))
                
            # print(lScan)
            
            # frens = huskyCount()
            # print(frens)
            # lidartest()
            