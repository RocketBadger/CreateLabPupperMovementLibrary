import multiprocessing
import time

from PupperAutomation.ActionLoop import ActionLoop
from PupperAutomation.MessageInjectionInterface import MessageInectionInterface
import PupperAutomation.preLoadedQueues as Demos
from PupperAutomation.run_robot import run_robot as robotLoop




def main():

   if __name__ == "__main__":

        robot_conn, transLoop_conn = multiprocessing.Pipe()
        injection_conn, transLoop_reciever_conn = multiprocessing.Pipe()

        actionLoop = ActionLoop(transLoop_conn, transLoop_reciever_conn)

        injectionInterface = MessageInectionInterface(injection_conn)

        # actionLoop.actionQueue = Demos.emptyQueue()# ny tom kø
        

        time.sleep(2)

        robot = multiprocessing.Process(target=robotLoop, args=(robot_conn, False,))
        transmission = multiprocessing.Process(target=actionLoop.start, args=())
        injecter = multiprocessing.Process(target=injectionInterface.injectionLoop, args=())

        
        # running processes
        robot.start()
        print("robot started")


        ## This sleep timer ensures that the robot is listening before the action transmission starts.
        time.sleep(1)
                
        transmission.start()
        print("transmis started")
        injecter.start()
        print("injector started")

        # wait until processes finish
        robot.join()
        print("robot joined started")
        transmission.join()
        print("transmission joined started")
        injecter.join()
        print("injector joined  started")

        robot.terminate()
        transmission.terminate()
        injecter.terminate()
        injecter.terminate()
 
 
main()
