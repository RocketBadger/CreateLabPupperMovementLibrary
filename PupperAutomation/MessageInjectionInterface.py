from multiprocessing import connection
from .behaviorFunctions import *

class MessageInjectionInterface:
    def __init__(self, ActionLoopConnection: connection.Connection):
        self.connection = ActionLoopConnection   
        
        self.connection.send(msg_Activation())

    # This is the main "do stuff" loop
    # Here you can change what the robot actually *does* during its runtime
    def injectionLoop(self):
        self.connection.send(msg_Trot(interrupt=False))

        while True:
            self.connection.send(msg_Forwards())