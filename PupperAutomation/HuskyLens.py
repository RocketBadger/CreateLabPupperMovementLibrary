from sensors.HuskyLens.huskylib import HuskyLensLibrary
from multiprocessing import connection

class HUSKYLENS:
    def __init__(self, injecter_connection: connection.Connection):
        self.connection = injecter_connection
        
        global husky
        # This port name has been configured by assigning fixed USB port names, to make sure the Pi finds the correct device for that USB port
        port = '/dev/ttyUSB_HUSKYLENS'
        husky = HuskyLensLibrary("SERIAL", port, 3000000)
        print("Woof!")
        
    def huskyCount():
        husky.algorthim("ALGORITHM_FACE_RECOGNITION")
        print(husky.count())
        return husky.count()
    
    def findPeople(self):
        husky.algorthim("ALGORITHM_FACE_RECOGNITION")
        while True:
            while (husky.count() > 0):
                if (husky.count() == 1):
                    self.connection.send(str(husky.count()) + " person found!")
                else:
                    self.connection.send(str(husky.count()) + " people found!")
            
    # Works but not all that well
    def findBall(self):
        husky.algorthim("ALGORITHM_OBJECT_TRACKING")
        while True:
            try:
                for block in husky.requestAll():
                    if block.getID() == 1 and block.learned:
                        husky.setCustomName("BALL", 1)
                        self.connection.send("BALL")
            except KeyboardInterrupt:
                print("Stopping HUSKY")
                self.connection.close()

                
    # saves a picture to SD Card upon finding object 
    def huskyTourist():
        husky.savePictureToSDCard()
            