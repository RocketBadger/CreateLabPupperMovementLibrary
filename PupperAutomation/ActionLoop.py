from .ActionMessage import *
from queue import Queue
from multiprocessing import connection


class ActionLoop:
    def __init__(self,  RobotConnection: connection.Connection, InjectionConnection: connection.Connection):
        """
            ActionLoop needs one end of a connection pipe tied to a Multiprocessing object.
        """

        self.robot_Connection = RobotConnection
        

        self.injecter_Connection = InjectionConnection

        # self.actionQueue = Queue()

        
    def start(self):
        """
            When called starts sending one message at a time from the actionQueue to the other end of the Multiprocessing pipe connection.
        """
        while True:
            
            ## Check for injections
            # if self.injecter_Connection.poll() == True:
            #     message: ActionMessage = self.injecter_Connection.recv()

                # if message.interrupt == True:
                #     self._handleInterruption(message)
                # else:
                #     self._handleInjection(message)

            ## check queue
            # if self.actionQueue.qsize() != 0:

                ## prepare message duration and sending
            # interruption: ActionMessage = None
            if self.injecter_Connection.poll() == True:
                # if interruption != None:
                #     currentActionMsg: ActionMessage = interruption
                #     interruption = None
                # else:
                currentActionMsg: ActionMessage = self.injecter_Connection.recv()
                ticks = currentActionMsg.ticks
                messageDone = False
                print(currentActionMsg.toDictionary())
                while messageDone == False:
                        ## Check for interrupting messages
                    self.robot_Connection.send(currentActionMsg.toDictionary())
                    # if self.injecter_Connection.poll() == True:
                    #     message: ActionMessage = self.injecter_Connection.recv()
                    #     if message.interrupt == True:
                    #             ## if message is an interrupt kill current queue, and build new with interruption message
                    #             # self._handleInterruption(message)
                    #         ticks == 0
                    #         messageDone = True
                    #         interruption: ActionMessage = message
                    #         break
                        # else:
                        #         # self._handleInjection(message)
                        #     print(currentActionMsg.toDictionary())
                        #     self.robot_Connection.send(currentActionMsg.toDictionary())
                    ticks -= 1
                    if ticks <= 0:
                        messageDone = True
            self.robot_Connection.send(ActionMessage().toDictionary())



    # def _handleInterruption(self, message: ActionMessage ):
    #     print("Intterrupt read, interrupting...")
    #     self.actionQueue = Queue()
    #     self.actionQueue.put(message)

        
    # def _handleInjection(self, message: ActionMessage):
    #     # print("Injection read and message queued")
    #     self.actionQueue.put(message)