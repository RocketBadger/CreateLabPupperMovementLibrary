from multiprocessing import connection
from .behaviorFunctions import *

class MessageInjectionInterface:
    def __init__(self, ActionLoopConnection: connection.Connection):
        self.connection = ActionLoopConnection   
        
        self.connection.send(msg_Activation())

    def injectionLoop(self):
        self.connection.send(msg_Trot(interrupt=False))

        while True:
            self.connection.send(msg_Forwards())