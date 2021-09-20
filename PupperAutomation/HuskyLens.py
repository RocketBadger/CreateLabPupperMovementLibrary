import serial
from sensors.HuskyLens.huskylib import HuskyLensLibrary
from serial.serialposix import Serial
from multiprocessing import connection

# def huskystart():
class HUSKYLENS:
    def __init__(self, injecter_connection: connection.Connection):
        self.connection = injecter_connection
        global husky
        # global husky_conn
        port = '/dev/ttyUSB_HUSKYLENS'
        husky = HuskyLensLibrary("SERIAL", port, 3000000)
        print("Woof!")
        
    def huskyCount():
        husky.algorthim("ALGORITHM_FACE_RECOGNITION")
        print(husky.count())
        return husky.count()
            
    # TODO
    # Works but could be more elegant
    def huskySniff(self):
        husky.algorthim("ALGORITHM_OBJECT_TRACKING")
        while True:
            try:
                # blocks=husky.requestAll()
                # x=0
                for block in husky.requestAll():
                    # print("Object ID: {} Learned: {}".format(str(block.getID()),str(block.learned)))
                    if block.getID() == 1 and block.learned:
                        husky.setCustomName("BALL", 1)
                        self.connection.send("BALL")
            except KeyboardInterrupt:
                print("Stopping HUSKY")
                self.connection.close()

                
    # saves a picture to SD Card upon finding object 
    def huskyTourist():
        husky.savePictureToSDCard()
            