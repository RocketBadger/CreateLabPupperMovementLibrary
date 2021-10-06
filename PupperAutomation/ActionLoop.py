from .ActionMessage import *
from multiprocessing import connection


class ActionLoop:
    def __init__(self,  RobotConnection: connection.Connection, InjectionConnection: connection.Connection):
        """
            ActionLoop needs one end of a connection pipe tied to a Multiprocessing object.
        """
        self.robot_Connection = RobotConnection
        self.injecter_Connection = InjectionConnection

    def start(self):
        """
            When called starts sending one message through the Multiprocessing pipe connection.
        """
        while True:
            if self.injecter_Connection.poll() == True:
                currentActionMsg: ActionMessage = self.injecter_Connection.recv()
                ticks = currentActionMsg.ticks
                messageDone = False
                
                print(currentActionMsg.toDictionary())
                
                while messageDone == False:
                    self.robot_Connection.send(currentActionMsg.toDictionary())
                    ticks -= 1
                    if ticks <= 0:
                        messageDone = True
            self.robot_Connection.send(ActionMessage().toDictionary())
