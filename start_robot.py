import multiprocessing
import time

from PupperAutomation.ActionLoop import ActionLoop
from PupperAutomation.MessageInjectionInterface import MessageInjectionInterface
from PupperAutomation.run_robot import run_robot as robotLoop
from PupperAutomation.LIDAR import LIDAR




def main():

   if __name__ == "__main__":

        robot_conn, transLoop_conn = multiprocessing.Pipe()
        injection_conn, transLoop_reciever_conn = multiprocessing.Pipe()
        actionLoop = ActionLoop(transLoop_conn, transLoop_reciever_conn)
        
        lidar_conn, lidar_injection_conn = multiprocessing.Pipe()
        
        injectionInterface = MessageInjectionInterface(injection_conn, lidar_conn)
        lidar = LIDAR(lidar_injection_conn)
        
        time.sleep(2)

        robot = multiprocessing.Process(target=robotLoop, args=(robot_conn, False,))
        transmission = multiprocessing.Process(target=actionLoop.start, args=())
        injecter = multiprocessing.Process(target=injectionInterface.injectionLoop, args=())
        lidar_pipe = multiprocessing.Process(target=lidar.lidarscan, args=())
        
        # running processes
        robot.start()
        print("robot started")


        ## This sleep timer ensures that the robot is listening before the action transmission starts.
        time.sleep(1)
                
        transmission.start()
        print("transmis started")
        injecter.start()
        print("injector started")
        lidar_pipe.start()
        print("LIDAR pipe")

        # wait until processes finish
        robot.join()
        print("robot joined")
        transmission.join()
        print("transmission joined")
        injecter.join()
        print("injector joined")
        lidar_pipe.join()
        print("LIDAR pipe joined")

        robot.terminate()
        transmission.terminate()
        injecter.terminate()
        # injecter.terminate()
 
 
main()
